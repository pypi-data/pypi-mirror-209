from collections.abc import Iterable
from datetime import datetime
from typing import Dict, List, Optional, Union
from attrs import define, field, asdict, validators
from dateutil.parser import parse
from datetime import date
from enum import Enum


class Mode(Enum):
    AR = "AR"
    AS = "AS"
    ASMT = "ASMT"
    AU = "AU"
    BDUS = "BDUS"
    BI = "BI"
    BMD = "BMD"
    CD = "CD"
    CF = "CF"
    CP = "CP"
    CR = "CR"
    CS = "CS"
    CT = "CT"
    DD = "DD"
    DF = "DF"
    DG = "DG"
    DM = "DM"
    DOC = "DOC"
    DS = "DS"
    DX = "DX"
    EC = "EC"
    ECG = "ECG"
    EPS = "EPS"
    ES = "ES"
    FA = "FA"
    FID = "FID"
    FS = "FS"
    GM = "GM"
    HC = "HC"
    HD = "HD"
    IO = "IO"
    IOL = "IOL"
    IVOCT = "IVOCT"
    IVUS = "IVUS"
    KER = "KER"
    KO = "KO"
    LEN = "LEN"
    LP = "LP"
    LS = "LS"
    MA = "MA"
    MG = "MG"
    MR = "MR"
    MS = "MS"
    NM = "NM"
    OAM = "OAM"
    OCT = "OCT"
    OP = "OP"
    OPM = "OPM"
    OPR = "OPR"
    OPT = "OPT"
    OPV = "OPV"
    OSS = "OSS"
    OT = "OT"
    PLAN = "PLAN"
    PR = "PR"
    PT = "PT"
    PX = "PX"
    REG = "REG"
    RESP = "RESP"
    RF = "RF"
    RG = "RG"
    RTDOSE = "RTDOSE"
    RTIMAGE = "RTIMAGE"
    RTPLAN = "RTPLAN"
    RTRECORD = "RTRECORD"
    RTSTRUCT = "RTSTRUCT"
    RWV = "RWV"
    SEG = "SEG"
    SM = "SM"
    SMR = "SMR"
    SR = "SR"
    SRF = "SRF"
    ST = "ST"
    STAIN = "STAIN"
    TG = "TG"
    US = "US"
    VA = "VA"
    VF = "VF"
    XA = "XA"
    XC = "XC"


def validator_pass(instance, attribute, value):
    pass


def calculate_age(birth_str: str) -> int:
    today = date.today()
    birth_date = parse(birth_str)
    return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))


def validator_parsable_date(instance, attribute, value):
    try:
        if value is not None:
            parse(value)
    except ValueError:
        raise ValueError("Unable to parse value")


@define(kw_only=True, slots=True, order=True, frozen=True)
class Instance:
    SOPinstanceUID: str = field(factory=str)


@define(kw_only=True, slots=True, order=True, frozen=True)
class Series:
    seriesUID: str = field(factory=str)
    instance_dict: Dict[str, Instance] = field(factory=dict)

    def add_instance(self, instance: Instance):
        if instance.SOPinstanceUID not in self.instance_dict.keys():
            self.instance_dict[instance.SOPinstanceUID] = instance

    def get_instance(self, instance_uid: Instance) -> Instance:
        return self.instance_dict[instance_uid]

    def get_dict(self):
        return asdict(self)

    def get_iter(self) -> Iterable:
        return iter(asdict(self))


@define(kw_only=True, slots=True, order=True, frozen=False)
class Study(dict):
    StudyUID: str = field(factory=str, validator=validator_pass)
    StudyInstanceUID: str = field(factory=str)
    SpecificCharacterSet: str = field(factory=str, validator=validator_pass)
    StudyDate: Optional[str] = field(default=None, validator=validator_parsable_date)
    StudyTime: Optional[str] = field(default=None, validator=validator_parsable_date)
    study_datetime: datetime = field(default=None, init=False, validator=validator_pass)
    AccessionNumber: str = field(factory=str, validator=validator_pass)
    ReferringPhysicianName: str = field(factory=str, validator=validator_pass)
    PatientName: str = field(factory=str, validator=validator_pass)
    PatientID: str = field(factory=str, validator=validator_pass)
    PatientBirthDate: Optional[str] = field(default=None, validator=validator_parsable_date)
    patient_age: int = field(default=None, init=False, validator=validator_pass)
    mode: Optional[Mode] = field(default=None, validator=validators.optional(validators.in_(Mode)))
    series_dict: Dict[str, Series] = field(factory=dict)

    def __attrs_post_init__(self):
        if self.StudyDate is not None:
            try:
                self.study_datetime = parse(self.StudyDate + " " + self.StudyTime)
            except ValueError:
                raise ValueError("Could not parse StudyDate:" + self.StudyDate + " or StudyTime:" + self.StudyTime)

        if self.PatientBirthDate is not None:
            self.patient_age = calculate_age(self.PatientBirthDate)

    def add_series(self, series: Series):
        if series.seriesUID not in self.series_dict.keys():
            self.series_dict[series.seriesUID] = series
        else:
            for instance in series.instance_dict.values():
                self.series_dict[series.seriesUID].add_instance(instance)

    def get_series_ids(self) -> list:
        return list(self.series_dict.keys())

    def get_series(self, seriesUID: str) -> dict:
        if seriesUID in self.series_dict.keys():
            return asdict(self.series_dict[seriesUID])

    def get_dict(self):
        return asdict(self)

    def get_iter(self) -> Iterable:
        return iter(asdict(self))
