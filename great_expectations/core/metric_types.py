import enum
import logging

logger = logging.getLogger(__name__)


class MetricDomainTypes(enum.Enum):
    TABLE = "table"
    COLUMN = "column"
    COLUMN_PAIR = "column_pair"
    MULTICOLUMN = "multicolumn"


class MetricFunctionTypes(enum.Enum):
    VALUE = "value"
    MAP_VALUES = "value"  # "map_values"
    WINDOW_VALUES = "value"  # "window_values"
    AGGREGATE_VALUE = "value"  # "aggregate_value"


class MetricPartialFunctionTypes(enum.Enum):
    MAP_FN = "map_fn"
    MAP_SERIES = "map_series"
    MAP_CONDITION_FN = "map_condition_fn"
    MAP_CONDITION_SERIES = "map_condition_series"
    WINDOW_FN = "window_fn"
    WINDOW_CONDITION_FN = "window_condition_fn"
    AGGREGATE_FN = "aggregate_fn"

    @property
    def metric_suffix(self) -> str:
        if self.name in ["MAP_FN", "MAP_SERIES", "WINDOW_FN"]:
            return "map"

        if self.name in [
            "MAP_CONDITION_FN",
            "MAP_CONDITION_SERIES",
            "WINDOW_CONDITION_FN",
        ]:
            return "condition"

        if self.name in ["AGGREGATE_FN"]:
            return "aggregate_fn"

        return ""
