import numpy as np
from typing import Any, Iterable
from .units import AxisInfo
from .axis import Axis

from . import ticker, units

class StrCategoryConverter(units.ConversionInterface):
    @staticmethod
    def convert(
        value: str | Iterable, unit: UnitData, axis: Axis
    ) -> float | np.ndarray: ...
    @staticmethod
    def axisinfo(unit: UnitData, axis: Axis) -> AxisInfo: ...
    @staticmethod
    def default_units(data: str, axis: Axis) -> UnitData: ...

class StrCategoryLocator(ticker.Locator):
    def __init__(self, units_mapping: dict[str, int]) -> None: ...
    def __call__(self): ...
    def tick_values(self, vmin, vmax) -> list: ...

class StrCategoryFormatter(ticker.Formatter):
    def __init__(self, units_mapping: dict[str, int]) -> None: ...
    def __call__(self, x, pos=...): ...
    def format_ticks(self, values)-> list[str]: ...

class UnitData:
    def __init__(self, data=...) -> None: ...
    def update(self, data: bytes)-> None: ...