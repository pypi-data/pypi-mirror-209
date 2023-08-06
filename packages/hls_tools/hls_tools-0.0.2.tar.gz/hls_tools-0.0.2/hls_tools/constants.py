from enum import Enum, IntEnum
from typing import Type, TypeVar

T = TypeVar("T", bound="StrEnum")


# NASA's STAC API
CMR_STAC_URL = "https://cmr.earthdata.nasa.gov/stac/LPCLOUD"


class StrEnum(str, Enum):
    """A string-based enum, that can lookup an enum value from a string.

    This is built-in in Python 3.11 but if you're not there yet...
    """

    @classmethod
    def from_str(cls: Type[T], s: str) -> T:
        """Look up an enum value by string."""
        for value in cls:
            if value == s:
                return value
        raise ValueError(f"Could not parse value from string: {s}")


class CollectionIDs(StrEnum):
    """Harmonized Landsat Sentinel collection IDs"""

    LANDSAT = "HLSL30.v2.0"
    SENTINEL = "HLSS30.v2.0"


class BandNames(StrEnum):
    """Harmonized Landsat Sentinel band common names"""

    COASTAL_AEROSOL = "coastal_aerosol"
    BLUE = "blue"
    GREEN = "green"
    RED = "red"
    RED_EDGE_1 = "red_edge_1"
    RED_EDGE_2 = "red_edge_2"
    RED_EDGE_3 = "red_edge_3"
    NIR_BROAD = "nir_broad"
    NIR_NARROW = "nir_narrow"
    SWIR_1 = "swir_1"
    SWIR_2 = "swir_2"
    CIRRUS = "cirrus"
    WATER_VAPOR = "water_vapor"
    THERMAL_INFRARED_1 = "thermal_infrared_1"
    THERMAL_INFRARED_2 = "thermal_infrared_2"
    FMASK = "Fmask"
    SAA = "solar_azimuth_angle"
    SZA = "solar_zenith_angle"
    VAA = "view_azimuth_angle"
    VZA = "view_zenith_angle"


class BandCodes(StrEnum):
    """Harmonized Landsat Sentinel band codes"""

    B01 = "B01"
    B02 = "B02"
    B03 = "B03"
    B04 = "B04"
    B05 = "B05"
    B06 = "B06"
    B07 = "B07"
    B08 = "B08"
    B8A = "B8A"
    B09 = "B09"
    B10 = "B10"
    B11 = "B11"
    B12 = "B12"
    SAA = "SAA"
    SZA = "SZA"
    VAA = "VAA"
    VZA = "VZA"


# dictionary to translate band codes to common names
BAND_CROSSWALK = {
    CollectionIDs.LANDSAT: {
        BandCodes.B01.value: BandNames.COASTAL_AEROSOL.value,
        BandCodes.B02.value: BandNames.BLUE.value,
        BandCodes.B03.value: BandNames.GREEN.value,
        BandCodes.B04.value: BandNames.RED.value,
        BandCodes.B05.value: BandNames.NIR_NARROW.value,
        BandCodes.B06.value: BandNames.SWIR_1.value,
        BandCodes.B07.value: BandNames.SWIR_2.value,
        BandCodes.B09.value: BandNames.CIRRUS.value,
        BandCodes.B10.value: BandNames.THERMAL_INFRARED_1.value,
        BandCodes.B11.value: BandNames.THERMAL_INFRARED_2.value,
        BandCodes.SAA.value: BandNames.SAA.value,
        BandCodes.SZA.value: BandNames.SZA.value,
        BandCodes.VAA.value: BandNames.VAA.value,
        BandCodes.VZA.value: BandNames.VZA.value,
    },
    CollectionIDs.SENTINEL: {
        BandCodes.B01.value: BandNames.COASTAL_AEROSOL.value,
        BandCodes.B02.value: BandNames.BLUE.value,
        BandCodes.B03.value: BandNames.GREEN.value,
        BandCodes.B04.value: BandNames.RED.value,
        BandCodes.B05.value: BandNames.RED_EDGE_1.value,
        BandCodes.B06.value: BandNames.RED_EDGE_2.value,
        BandCodes.B07.value: BandNames.RED_EDGE_3.value,
        BandCodes.B08.value: BandNames.NIR_BROAD.value,
        BandCodes.B8A.value: BandNames.NIR_NARROW.value,
        BandCodes.B09.value: BandNames.WATER_VAPOR.value,
        BandCodes.B10.value: BandNames.CIRRUS.value,
        BandCodes.B11.value: BandNames.SWIR_1.value,
        BandCodes.B12.value: BandNames.SWIR_2.value,
        BandCodes.SAA.value: BandNames.SAA.value,
        BandCodes.SZA.value: BandNames.SZA.value,
        BandCodes.VAA.value: BandNames.VAA.value,
        BandCodes.VZA.value: BandNames.VZA.value,
    },
}


class FmaskBitFields(IntEnum):
    """HLS Fmask bit fields"""

    CIRRUS = 0
    CLOUD = 1
    ADJACENT_TO_CLOUD_OR_SHADOW = 2
    CLOUD_SHADOW = 3
    SNOW_ICE = 4
    WATER = 5
    # AEROSOL_LEVEL = [6, 7] # TODO: figure out how to represent these


class FmaskBitValues(IntEnum):
    NO = 0
    YES = 1

    # aerosol levels
    # CLIMATOLOGY_AEROSOL = [0, 0]
    # LOW_AEROSOL = [0, 1]
    # MODERATE_AEROSOL = [1, 0]
    # HIGH_AEROSOL = [1, 1]
