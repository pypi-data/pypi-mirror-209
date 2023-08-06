
from enum import Enum
from pydantic import BaseModel



class ErrorTypes(Enum):
    AgencyError: int = 0
    AgencyErrorDuplicateID: int = 1
    AgencyErrorInvalidAgency: int = 2

    GTFSError: int = 100
    GTFSErrorInvalidFile: int = 101
    GTFSErrorUnknownFile: int = 102
    GTFSErrorProcessReturnedFalse: int = 103

    StopError: int = 200
    StopErrorDuplicateID: int = 201
    StopErrorInvalidStop: int = 202



class AgencyError(BaseModel):
    caller: str = "Agency"
    name: str = "AgencyError"
    error_type: ErrorTypes = ErrorTypes.AgencyError
    message: str
    values: list = []



class GTFSError(BaseModel):
    caller: str = "GTFS"
    name: str = "GTFSError"
    error_type: ErrorTypes = ErrorTypes.GTFSError
    message: str
    values: list = []



class StopError(BaseModel):
    caller: str = "Stop"
    name: str = "StopError"
    errory_type: ErrorTypes = ErrorTypes.StopError
    message: str
    values: list = []
