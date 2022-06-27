from enum import unique
from ts_t1_validator.models.enums.abstract_enum import AbstractEnum


@unique
class StrategyTypeEnum(AbstractEnum):
    REM = "REM"
    GBO = "GBO"
    AUD = "AUD"
    UNDEFINED = None
