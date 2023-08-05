""" schema describing imaging instrument """

from __future__ import annotations

from datetime import date
from enum import Enum
from typing import List, Optional

from pydantic import Field

from ..base import AindCoreModel, AindModel
from ..device import Coupling, DAQDevice, DataInterface, Device, Filter, Manufacturer, PowerUnit, SizeUnit


class Com(AindModel):
    """Description of a communication system"""

    hardware_name: str = Field(..., title="Controlled hardware device")
    com_port: str = Field(..., title="COM port")


class CameraType(Enum):
    """Camera type name"""

    CAMERA = "Camera"
    PMT = "PMT"
    OTHER = "other"


class Cooling(Enum):
    """Cooling medium name"""

    AIR = "air"
    WATER = "water"


class Detector(Device):
    """Description of a detector device"""

    type: CameraType = Field(..., title="Detector type")
    data_interface: DataInterface = Field(..., title="Data interface")
    cooling: Cooling = Field(..., title="Cooling")


class LightsourceType(Enum):
    """Light source type name"""

    LAMP = "lamp"
    LASER = "laser"
    LED = "LED"
    OTHER = "other"


class Lightsource(Device):
    """Description of lightsource device"""

    type: LightsourceType = Field(..., title="Lightsource Type")
    coupling: Coupling = Field(..., title="Coupling")
    wavelength: float = Field(..., title="Wavelength (nm)", units="nm", ge=300, le=1000)
    wavelength_unit: SizeUnit = Field(SizeUnit.NM, title="Wavelength unit")
    max_power: float = Field(..., title=" Maximum power (mW)", units="mW")
    power_unit: PowerUnit = Field(PowerUnit.MW, title="Power unit")


class Immersion(Enum):
    """Immersion media name"""

    AIR = "air"
    MULTI = "multi"
    OIL = "oil"
    WATER = "water"
    OTHER = "other"


class Objective(Device):
    """Description of an objective device"""

    numerical_aperture: float = Field(..., title="Numerical aperture (in air)")
    magnification: float = Field(..., title="Magnification")
    immersion: Immersion = Field(..., title="Immersion")


class ImagingDeviceType(Enum):
    """Imaginge device type name"""

    BEAM_EXPANDER = "Beam expander"
    DIFFUSER = "Diffuser"
    GALVO = "Galvo"
    LASER_COMBINER = "Laser combiner"
    LASER_COUPLER = "Laser coupler"
    PRISM = "Prism"
    OBJECTIVE = "Objective"
    ROTATION_MOUNT = "Rotation mount"
    SLIT = "Slit"
    TUNABLE_LENS = "Tunable lens"
    OTHER = "Other"


class ImagingInstrumentType(Enum):
    """Experiment type name"""

    CONFOCAL = "confocal"
    DISPIM = "diSPIM"
    EXASPIM = "exaSPIM"
    ECEPHYS = "ecephys"
    MESOSPIM = "mesoSPIM"
    OTHER = "Other"
    SMARTSPIM = "SmartSPIM"
    TWO_PHOTON = "Two photon"


class AdditionalImagingDevice(Device):
    """Description of additional devices"""

    type: ImagingDeviceType = Field(..., title="Device type")


class StageAxisDirection(Enum):
    """Direction of motion for motorized stage"""

    DETECTION_AXIS = "Detection axis"
    ILLUMINATION_AXIS = "Illumination axis"
    PERPENDICULAR_AXIS = "Perpendicular axis"


class StageAxisName(Enum):
    """Axis names for motorized stages as configured by hardware"""

    X = "X"
    Y = "Y"
    Z = "Z"


class MotorizedStage(Device):
    """Description of motorized stage"""

    travel: float = Field(..., title="Travel of device (mm)", units="mm")
    travel_unit: SizeUnit = Field(SizeUnit.MM, title="Travel unit")


class ScanningStage(MotorizedStage):
    """Description of a scanning motorized stages"""

    stage_axis_direction: StageAxisDirection = Field(..., title="Direction of stage axis")
    stage_axis_name: StageAxisName = Field(..., title="Name of stage axis")


class OpticalTable(Device):
    """Description of Optical Table"""

    length: Optional[float] = Field(None, title="Length (inches)", units="inches", ge=0)
    width: Optional[float] = Field(None, title="Width (inches)", units="inches", ge=0)
    table_size_unit: SizeUnit = Field(SizeUnit.IN, title="Table size unit")
    vibration_control: Optional[bool] = Field(None, title="Vibration control")


class Instrument(AindCoreModel):
    """Description of an instrument, which is a collection of devices"""

    schema_version: str = Field("0.5.5", description="schema version", title="Version", const=True)
    instrument_id: Optional[str] = Field(
        None,
        description="unique identifier for this instrument configuration",
        title="Instrument ID",
    )
    instrument_type: ImagingInstrumentType = Field(..., title="Instrument type")
    location: str = Field(..., title="Instrument location")
    manufacturer: Manufacturer = Field(..., title="Instrument manufacturer")
    temperature_control: Optional[bool] = Field(None, title="Temperature control")
    humidity_control: Optional[bool] = Field(None, title="Humidity control")
    optical_tables: List[OpticalTable] = Field(None, title="Optical table")
    objectives: List[Objective] = Field(..., title="Objectives", unique_items=True)
    detectors: Optional[List[Detector]] = Field(None, title="Detectors", unique_items=True)
    light_sources: Optional[List[Lightsource]] = Field(None, title="Light sources", unique_items=True)
    fluorescence_filters: Optional[List[Filter]] = Field(None, title="Fluorescence filters", unique_items=True)
    motorized_stages: Optional[List[MotorizedStage]] = Field(None, title="Motorized stages", unique_items=True)
    scanning_stages: Optional[List[ScanningStage]] = Field(None, title="Scanning motorized stages", unique_items=True)
    daqs: Optional[List[DAQDevice]] = Field(None, title="DAQ", unique_items=True)
    additional_devices: Optional[List[AdditionalImagingDevice]] = Field(
        None, title="Additional devices", unique_items=True
    )
    calibration_date: Optional[date] = Field(
        None,
        description="Date of most recent calibration",
        title="Calibration date",
    )
    calibration_data: Optional[str] = Field(
        None,
        description="Path to calibration data from most recent calibration",
        title="Calibration data",
    )
    com_ports: Optional[List[Com]] = Field(None, title="COM ports", unique_items=True)
    notes: Optional[str] = None
