# feed.py

import datetime as dt
from typing import (
    Dict, Optional, Iterable, Any,
    Union, Callable, List
)

import pandas as pd

from cryptofeed import FeedHandler
from cryptofeed.types import OrderBook
from cryptofeed.exchanges import EXCHANGE_MAP
from cryptofeed.defines import L2_BOOK

from auto_screener.dataset import BIDS, ASKS
from auto_screener.tickers import Separator
from auto_screener.screener import BaseScreener
from auto_screener.hints import Number

__all__ = [
    "MarketRecorder",
    "add_feeds",
    "create_market"
]

Market = Dict[str, Dict[str, pd.DataFrame]]
RecorderParameters = Dict[str, Union[Iterable[str], Dict[str, Callable]]]

def create_market(data: Dict[str, Iterable[str]]) -> Dict[str, Dict[str, pd.DataFrame]]:
    """
    Creates the dataframes of the market data.

    :param data: The market data.

    :return: The dataframes of the market data.
    """

    return {
        source: {
            ticker: pd.DataFrame({BIDS: [], ASKS: []}, index=[])
            for ticker in data[source]
        } for source in data
    }
# end create_market

class MarketRecorder:
    """A class to represent a crypto data feed recorder."""

    def __init__(self, market: Optional[Market] = None) -> None:
        """
        Defines the class attributes.

        :param market: The object to fill with the crypto feed record.
        """

        self.market: Market = market or {}
    # end __init__

    def parameters(self) -> RecorderParameters:
        """
        Returns the order book parameters.

        :return: The order book parameters.
        """

        return dict(
            channels=[L2_BOOK],
            callbacks={L2_BOOK: self.record}
        )
    # end parameters

    async def record(self, data: OrderBook, timestamp: float) -> None:
        """
        Records the data from the crypto feed into the dataset.

        :param data: The data from the exchange.
        :param timestamp: The time of the request.
        """

        dataset = (
            self.market.
            setdefault(data.exchange, {}).
            setdefault(
                data.symbol.replace('-', Separator.value),
                pd.DataFrame({BIDS: [], ASKS: []}, index=[])
            )
        )

        try:
            dataset.loc[dt.datetime.fromtimestamp(timestamp)] = {
                BIDS: data.book.bids.index(0)[0],
                ASKS: data.book.asks.index(0)[0]
            }

        except IndexError:
            return
        # end try
    # end record

    def screener(
            self,
            ticker: str,
            source: str,
            location: Optional[str] = None,
            cancel: Optional[Union[Number, dt.timedelta]] = None,
            delay: Optional[Union[Number, dt.timedelta]] = None
    ) -> BaseScreener:
        """
        Defines the class attributes.

        :param ticker: The ticker of the asset.
        :param source: The exchange to get source data from.
        :param location: The saving location for the data.
        :param cancel: The time to cancel the waiting.
        :param delay: The delay for the process.
        """

        if source not in self.market:
            raise ValueError(
                f"source {source} is not a valid exchange in {self}."
            )
        # end if

        if ticker not in self.market[source]:
            raise ValueError(
                f"ticker {ticker} of exchange {source} "
                f"is not a valid ticker in {self}."
            )
        # end if

        screener = BaseScreener(
            ticker=ticker, source=source, delay=delay,
            location=location, cancel=cancel
        )

        screener.market = self.market[source][ticker]

        return screener
    # end screener

    def screeners(
            self,
            location: Optional[str] = None,
            cancel: Optional[Union[Number, dt.timedelta]] = None,
            delay: Optional[Union[Number, dt.timedelta]] = None
    ) -> List[BaseScreener]:
        """
        Defines the class attributes.

        :param location: The saving location for the data.
        :param cancel: The time to cancel the waiting.
        :param delay: The delay for the process.
        """

        base_screeners = []

        for source in self.market:
            for ticker in self.market[source]:
                base_screeners.append(
                    self.screener(
                        ticker=ticker, source=source, delay=delay,
                        location=location, cancel=cancel
                    )
                )
            # end for
        # end for

        return base_screeners
    # end screeners
# end MarketRecorder

def add_feeds(
        handler: FeedHandler,
        data: Dict[str, Iterable[str]],
        fixed: Optional[bool] = False,
        separator: Optional[str] = Separator.value,
        parameters: Optional[Dict[str, Dict[str, Any]]] = None
) -> None:
    """
    Adds the tickers to the handler for each exchange.

    :param handler: The handler object.
    :param data: The data of the exchanges and tickers to add.
    :param parameters: The parameters for the exchanges.
    :param fixed: The value for fixed parameters to all exchanges.
    :param separator: The separator of the assets.
    """

    base_parameters = None

    if not fixed:
        parameters = parameters or {}

    else:
        base_parameters = parameters or {}
        parameters = {}
    # end if

    for exchange, tickers in data.items():
        exchange = exchange.upper()

        tickers = [
            ticker.replace(separator, '-')
            for ticker in tickers
        ]

        if fixed:
            parameters.setdefault(exchange, base_parameters)
        # end if

        handler.add_feed(
            EXCHANGE_MAP[exchange](
                symbols=tickers,
                **(
                    parameters[exchange]
                    if (
                        (exchange in parameters) and
                        isinstance(parameters[exchange], dict) and
                        all(isinstance(key, str) for key in parameters)

                    ) else {}
                )
            )
        )
    # end for
# end add_feeds