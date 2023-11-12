#!/usr/bin/python
##-------------------------------##
## PyTrader                      ##
## Written By: Ryan Smith        ##
##-------------------------------##
## Strategy                      ##
##-------------------------------##

## Imports
from abc import ABC, abstractmethod


## Classes
class Strategy:
    """
    """

    # -Constructor
    def __init__(self) -> None:
        pass

    # -Dunder Methods
    def __repr__(self) -> str:
        return ""

    def __str__(self) -> str:
        return ""

    # -Instance Methods
    @abstractmethod
    def on_candle(self) -> None:
        pass

    def buy(self) -> None:
        ''''''
        pass

    def sell(self) -> None:
        ''''''
        pass
