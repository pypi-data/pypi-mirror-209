"""hls-tools: tools for working with the Harmonized Landsat Sentinel 2 dataset"""
__version__ = "0.0.2"

import os
from datetime import datetime
from typing import List, Tuple, Union

import pystac
import pystac_client
import rasterio.crs
import stackstac
import xarray as xr
from rasterio import warp

from .constants import (
    CMR_STAC_URL,
    BAND_CROSSWALK,
    BandNames,
    CollectionIDs,
    FmaskBitFields,
    FmaskBitValues,
)

ALL_BANDS = [band.value for band in list(BandNames)]
EPSG_4326 = rasterio.crs.CRS.from_epsg(4326)

# TODO: make these safe for windows
NETRC_PATH = os.path.expanduser("~/.netrc")
COOKIE_FILE = "/tmp/cookies.txt"


def flatten(x: xr.DataArray, dim: str = "time") -> xr.DataArray:
    """Convenience function to flatten a DataArray to have one time coordinate per
    unique value on the time dimension. This helps prepare DataArrays for further
    processing where having duplicate values of a dimension like time might cause
    issues
    """
    assert isinstance(x, xr.DataArray)
    if len(x[dim].values) > len(set(x[dim].values)):
        x = x.groupby(dim).map(stackstac.mosaic)

    assert isinstance(x, xr.DataArray)

    return x


def query_hls_catalog(
    bbox: Tuple[float, float, float, float],
    crs: rasterio.crs.CRS,
    start_date: datetime,
    end_date: datetime,
) -> pystac.ItemCollection:
    catalog = pystac_client.Client.open(CMR_STAC_URL)

    bbox_4326 = warp.transform_bounds(
        crs,
        EPSG_4326,
        *bbox,
    )

    return catalog.search(
        collections=[CollectionIDs.LANDSAT, CollectionIDs.SENTINEL],
        bbox=bbox_4326,
        datetime=[start_date, end_date],
    ).item_collection()


def translate_asset_keys(
    hls_stac_items: pystac.ItemCollection,
) -> pystac.ItemCollection:
    """Update HLS STAC item metadata so that asset keys correspond to band common names
    instead of band codes, which makes to make it easy to load Landsat and Sentinel data
    together.
    """
    for item in hls_stac_items:
        band_dict = BAND_CROSSWALK.get(CollectionIDs.from_str(str(item.collection_id)))
        assert band_dict

        for original_band, new_band in band_dict.items():
            if item.assets.get(original_band):
                item.assets[new_band] = item.assets.pop(original_band)

    return hls_stac_items


def load_hls_stack(
    bbox: Tuple[float, float, float, float],
    crs: rasterio.crs.CRS,
    start_date: Union[datetime, None] = None,
    end_date: Union[datetime, None] = None,
    stac_items: Union[pystac.ItemCollection, None] = None,
    bands: List[str] = ALL_BANDS,
    resolution: float = 30,
) -> xr.DataArray:
    for band in bands:
        assert (
            band in ALL_BANDS
        ), f"{band} not available, please chose from one of " + ", ".join(ALL_BANDS)

    if not stac_items:
        assert start_date, "you must provide a datetime for start_date"
        assert end_date, "you must provide a datetime for end_date"
        stac_items = query_hls_catalog(
            bbox=bbox, crs=crs, start_date=start_date, end_date=end_date
        )

    hls_stack = stackstac.stack(
        items=translate_asset_keys(stac_items),
        assets=bands,
        bounds=bbox,
        epsg=crs.to_epsg(),
        resolution=resolution,
        xy_coords="center",
        gdal_env=stackstac.DEFAULT_GDAL_ENV.updated(
            always=dict(
                CPL_VSIL_CURL_USE_HEAD=False,
                GDAL_HTTP_COOKIEJAR=COOKIE_FILE,
                GDAL_HTTP_COOKIEFILE=COOKIE_FILE,
            )
        ),
    )

    return flatten(hls_stack, dim="time")


def mask_out_clouds(hls_stack: xr.DataArray) -> xr.DataArray:
    """Replace pixels classified by Fmask as clouds, cloud shadows, or adjacent
    to clouds or shadows with NaN
    """
    is_cloud_or_shadow = 0
    for field in [
        FmaskBitFields.CLOUD,
        FmaskBitFields.CLOUD_SHADOW,
        FmaskBitFields.ADJACENT_TO_CLOUD_OR_SHADOW,
    ]:
        is_cloud_or_shadow |= FmaskBitValues.YES << field

    fmask = hls_stack.sel(band=BandNames.FMASK).astype("uint16")
    clouds_and_shadows = fmask & is_cloud_or_shadow

    return hls_stack.where(clouds_and_shadows == 0)


def mask_to_water(hls_stack: xr.DataArray) -> xr.DataArray:
    is_water = FmaskBitValues.YES << FmaskBitFields.WATER

    fmask = hls_stack.sel(band=BandNames.FMASK).astype("uint16")
    water = fmask & is_water

    return hls_stack.where(water != 0)
