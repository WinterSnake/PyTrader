#!/usr/bin/python
##-------------------------------##
## PyTrader                      ##
## Written By: Ryan Smith        ##
##-------------------------------##
## Backtest                      ##
##-------------------------------##

## Imports
from .account import Account
from .broker import Broker
from .strategy import Strategy


## Classes
class Backtester:
    """
    """

    # -Constructor
    def __init__(
        self, account: Account, broker: Broker, strategy: Strategy
    ) -> None:
        self.account: Account = account
        self.broker: Broker = broker
        self.strategy: Strategy = strategy

    # -Dunder Methods
    def __repr__(self) -> str:
        return ""

    def __str__(self) -> str:
        return ""

    # -Instance Methods
    def run(self) -> None:
        ''''''
        pass

    def tick(self) -> None:
        ''''''
        pass
