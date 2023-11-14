#!/usr/bin/python
##-------------------------------##
## PyTrader                      ##
## Written By: Ryan Smith        ##
##-------------------------------##
## Account                       ##
##-------------------------------##

## Imports
from .broker import Order

## Constants
__all__: tuple[str] = ("Account",)


## Classes
class Account:
    """
    """

    # -Constructor
    def __init__(self, balance: float, can_short: bool = False, margin: float | None = None) -> None:
        self.balance: float = balance
        self.orders: list[Order] = []

    # -Instance Methods
    def tick(self) -> None:
        '''Tick account'''
        for order in self.orders:
            order.tick()
