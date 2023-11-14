#!/usr/bin/python
##-------------------------------##
## PyTrader: Broker              ##
## Written By: Ryan Smith        ##
##-------------------------------##
## Order                         ##
##-------------------------------##

## Imports
from __future__ import annotations

## Constants
__all__: tuple[str] = ("Order",)


## Classes
class Order:
    """
    """

    # -Constructor
    def __init__(self) -> None:
        self.filled: bool = False
        self.expected_quantity: int

    # -Instance Methods
    def cancel(self) -> bool:
        ''''''
        pass

    def close(self) -> Order:
        ''''''
        pass

    def tick(self) -> None:
        ''''''
        pass
