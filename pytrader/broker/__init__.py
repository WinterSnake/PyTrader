#!/usr/bin/python
##-------------------------------##
## PyTrader: Broker              ##
## Written By: Ryan Smith        ##
##-------------------------------##

## Imports
import polars

from .order import Order
from .future import Future

## Constants
__all__: tuple[str, ...] = (
    "Broker", "Future", "Order",
)


## Classes
class Broker:
    """
    """

    # -Constructor
    def __init__(self) -> None:
        self.futures: list[Future] = []

    # -Instance Methods
    def add_future(
        self, symbol: str, historicals: polars.DataFrame, value: float,
        ticks: int, margin: float, maintenance: float, commission: float
    ) -> None:
        ''''''
        pass

    def tick(self) -> None:
        ''''''
        pass
