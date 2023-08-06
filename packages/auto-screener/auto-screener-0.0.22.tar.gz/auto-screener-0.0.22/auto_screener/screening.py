# screening.py

import os
import time
import asyncio
import warnings
import datetime as dt
import threading
from typing import (
    Optional, Union, Dict, Iterable, Any, List, Set
)

import pandas as pd
import numpy as np

import ccxt
import ccxt.pro as ccxtpro
import ccxt.async_support as async_ccxt

from represent import BaseModel, Modifiers

from auto_screener.hints import Number
from auto_screener.dataset import (
    OPEN, HIGH, LOW, CLOSE, VOLUME, BIDS, ASKS,
    row_to_dataset, DATE_TIME, OHLCV_COLUMNS
)
from auto_screener.base import terminate_thread
from auto_screener.interval import interval_to_total_time
from auto_screener.screener import (
    wait_for_update, WaitingState, AutoDataCollector, BaseScreener,
    wait_for_dynamic_update, wait_for_dynamic_initialization
)

__all__ = [
    "AutoDataset",
    "AutoScreener",
    "MultiScreener",
    "ScreenerSignature",
    "live_screeners"
]

def configure_exchange(
        source: str,
        pro: Optional[bool] = True,
        options: Optional[Dict[str, Any]] = None
):
    """
    Validates the exchange source value.

    :param source: The name of the exchange platform.
    :param pro: The value for the pro interface.
    :param options: The ccxt options.

    :return: The validates source.
    """

    try:
        exchange = getattr(
            (ccxtpro if pro else async_ccxt), source
        )(options)

    except AttributeError:
        raise ValueError(f"Unrecognized exchange name: {source}.")
        # end try

    if not (
            hasattr(exchange, "watch_tickers") or
            hasattr(exchange, "fetch_tickers")
    ):
        raise ValueError(
            f"Exchange {exchange} must have at least one of the "
            f"methods 'fetch_tickers', or 'watch_tickers'."
        )
        # end if
    # end if

    return exchange
# end configure_exchange

class AutoScreener(BaseScreener):
    """
    A class to represent an asset price screener.

    Using this class, you can create a screener object to
    screen the market ask and bid data for a specific asset in
    a specific exchange at real time.

    Parameters:

    - ticker:
        The ticker symbol of an asset to screen.

    - source:
        The name of the exchange platform to screen data from.

    - delay:
        The delay to wait between each data fetching.

    - pro:
        The value to use the pro interface.

    - options:
        The ccxt options for the backend screening process.

    - locaion:
        The saving location for the saved data of the screener.

    - cencel:
        The time to cancel screening process after no new data is fetched.

    >>> from auto_screener.screening import AutoScreener
    >>> from auto_screener.screener import wait_for_initialization
    >>>
    >>> screener = AutoScreener(
    >>>     ticker="BTC/USD", source="binance"
    >>> )
    >>>
    >>> screener.run(wait=True)
    >>>
    >>> while True:
    >>>     print(screener.market.iloc[-1])
    >>>
    >>>     wait_for_update(screener, delay=1)
    """

    COLUMNS = (
        OPEN, HIGH, LOW, CLOSE,
        ASKS, BIDS, VOLUME
    )

    def __init__(
            self,
            ticker: str,
            source: str,
            pro: Optional[bool] = True,
            delay: Optional[Union[Number, dt.timedelta]] = None,
            options: Optional[Dict[str, Any]] = None,
            location: Optional[str] = None,
            cancel: Optional[Union[Number, dt.timedelta]] = None
    ) -> None:
        """
        Defines the class attributes.

        :param ticker: The ticker of the asset.
        :param source: The exchange to get source data from.
        :param delay: The delay for the process.
        :param location: The saving location for the data.
        :param pro: The value for the pro interface.
        :param options: The ccxt options.
        :param cancel: The time to cancel the waiting.
        """

        self.options = options or {}

        self.delay = delay or self.DELAY

        self.pro = pro

        self.task = None

        super().__init__(
            ticker=ticker, source=source,
            location=location, cancel=cancel
        )

        self.market = pd.DataFrame(
            {column: [] for column in self.COLUMNS}, index=[]
        )

        self.market.index.name = DATE_TIME
    # end __init__

    def __getstate__(self) -> Dict[str, Any]:
        """
        Returns the data of the object.

        :return: The state of the object.
        """

        data = self.__dict__.copy()

        data["screening_process"] = None
        data["timeout_process"] = None
        data["task"] = None

        return data
    # end __getstate__

    async def async_get_market(self) -> Dict[str, Number]:
        """
        Gets the market data.

        :return: The bids and asks.
        """

        exchange = configure_exchange(
            source=self.source.lower(), pro=self.pro,
            options=self.options
        )

        method = None

        if hasattr(exchange, "fetch_tickers"):
            method = exchange.fetch_tickers

        elif hasattr(exchange, "watch_tickers"):
            method = exchange.watch_tickers
        # end if

        data = await method(symbols=[self.ticker])

        ticker = list(data.keys())[0]

        data[ticker][VOLUME.lower()] = data[ticker]["quoteVolume"]
        data[ticker][self.ASKS.lower()] = data[ticker]["ask"]
        data[ticker][self.BIDS.lower()] = data[ticker]["bid"]

        data = {
            key: data[ticker][key.lower()] for key in
            self.COLUMNS
        }

        if any(np.isnan(value) for value in data.values()):
            ohlcv = await exchange.fetch_ohlcv(
                self.ticker, timeframe='1m', limit=1
            )

            ohlcv = {
                column: value for column, value in zip(
                    [OPEN, HIGH, LOW, CLOSE, VOLUME], ohlcv
                ) if np.isnan(data[column])
            }

            data.update(ohlcv)
        # end if

        if isinstance(exchange, getattr(ccxtpro, self.source)):
            await exchange.close()
        # end if

        return data
    # end async_get_market

    async def async_update_market(self) -> None:
        """Updates the market data."""

        data = await self.async_get_market()

        self.market.loc[dt.datetime.now()] = data
    # end async_update_market

    def update_market(self) -> None:
        """Updates the market data."""

        asyncio.run(self.async_update_market())
    # end update_market

    def get_market(self) -> Dict[str, Number]:
        """Gets the market data."""

        return asyncio.run(self.async_get_market())
    # end get_market

    async def async_run_loop(self) -> None:
        """Runs the processes of price screening."""

        self.running = True

        delay = self.delay

        if isinstance(delay, dt.timedelta):
            delay = delay.total_seconds()
        # end if

        while self.running:
            start = time.time()

            try:
                await self.async_update_market()

            except Exception as e:
                self.terminate()

                raise RuntimeError(
                    f"Could not complete task. {str(e)}"
                ) from e
            # end try

            end = time.time()

            if delay:
                time.sleep(max([delay - (end - start), 0]))
            # end if
        # end while
    # end async_run

    def run_loop(self) -> None:
        """Runs the process of the price screening."""

        task = self.async_run_loop()

        try:
            loop = asyncio.get_event_loop()

            self.task = loop.create_task(task)

            if not loop.is_running():
                loop.run_forever()
            # end if

        except RuntimeError:
            asyncio.run(task)
        # end try
    # end run_loop

    def run_new_loop(self) -> None:
        """Runs the process of the price screening."""

        task = self.async_run_loop()

        try:
            loop = asyncio.new_event_loop()

            self.task = loop.create_task(task)

            if not loop.is_running():
                loop.run_forever()
            # end if

        except RuntimeError:
            asyncio.run(task)
        # end try
    # end run_loop

    def stop(self) -> None:
        """Stops the screening process."""

        super().stop()

        if self.task is not None:
            self.task.cancel()
        # end if
# end Screener

class ScreenerSignature(BaseModel):
    """
    A class to represent a screener signature.

    Parameters:

    - ticker:
        The ticker symbol of an asset to screen.

    - source:
        The name of the exchange platform to screen data from.

    - delay:
        The delay to wait between each data fetching.

    - pro:
        The value to use the pro interface.
    """

    def __init__(
            self,
            ticker: str,
            source: str,
            pro: bool,
            delay: Union[Number, dt.timedelta]
    ) -> None:
        """
        Defines the class attributes.

        :param ticker: The ticker of the asset.
        :param source: The exchange to get source data from.
        :param delay: The delay for the process.
        :param pro: The value for the pro interface.
        """

        self.ticker = ticker
        self.source = source

        self.pro = pro

        self.delay = delay
    # end __init__
# end ScreenerSignature

def ohlcv_to_dataset(data: Iterable[Iterable]) -> pd.DataFrame:
    """
    Adjusts the dataset to an asset Open, High, Low, Close, Bids, Asks, Volume dataset.

    :param data: The data to adjust.

    :return: The asset dataset.
    """

    data = pd.DataFrame(data)

    index_column_name = list(data.columns)[0]

    data.index = pd.to_datetime(data[index_column_name], unit="ms")
    del data[index_column_name]
    data.index.name = DATE_TIME
    data.columns = list(OHLCV_COLUMNS)

    return data
# end ohlcv_to_dataset

class AutoDataset(BaseScreener):
    """
    A class to represent a live asset data builder.

    Using this class, you can create a screener object to
    screen the market ask and bid data for a specific asset in
    a specific exchange at real time.

    You can also use it to build real time datasets of Open
    High Low Close Volume, with Bids and Asks.

    Parameters:

    - ticker:
        The ticker symbol of an asset to screen.

    - source:
        The name of the exchange platform to screen data from.

    - locaion:
        The saving location for the saved data of the screener.

    - interval:
        The interval for the time between data points in the dataset.

    - delay:
        The delay to wait between each data fetching.

    - screener:
        The screener object to connect to for creating the dataset.

    - length:
        An initial dataset length to start with.

    - pro:
        The value to use the pro interface.

    - options:
        The ccxt options for the backend screening process.

    - cencel:
        The time to cancel screening process after no new data is fetched.

    >>> from auto_screener.screening import AutoDataset
    >>> from auto_screener.screener import wait_for_initialization
    >>> from auto_screener.interval import interval_to_total_time
    >>>
    >>> interval = "1m"
    >>>
    >>> dataset = AutoDataset(
    >>>     ticker="BTC/USD", source="binance", interval=interval
    >>> )
    >>>
    >>> dataset.run(wait=True)
    >>>
    >>> print(dataset.market.iloc[-1].splitlines()[0])
    >>>
    >>> while True:
    >>>     print(dataset.market.iloc[-1].splitlines()[-1])
    >>>
    >>>     wait_for_update(dataset, delay=interval_to_total_time(interval))
    """

    modifiers = Modifiers(
        excluded=[
            "timeout_process", 'market', 'built',
            'exchange', 'screening_process', "delay"
        ]
    )

    screeners: Dict[ScreenerSignature, AutoScreener] = {}

    COLUMNS = AutoScreener.COLUMNS

    DELAY = 1
    CANCEL = 60

    def __init__(
            self,
            ticker: str,
            source: str,
            interval: str,
            pro: Optional[bool] = True,
            data: Optional[pd.DataFrame] = None,
            length: Optional[Union[bool, int]] = None,
            delay: Optional[Union[Number, dt.timedelta]] = None,
            location: Optional[str] = None,
            screener: Optional[BaseScreener] = None,
            options: Optional[Dict[str, Any]] = None,
            cancel: Optional[Union[Number, dt.timedelta]] = None
    ) -> None:
        """
        Defines the class attributes.

        :param ticker: The ticker of the asset.
        :param source: The exchange to get source data from.
        :param interval: The interval for the data.
        :param data: The base dataset of the asset to add to.
        :param length: The length of the base dataset.
        :param location: The saving location for the data.
        :param delay: The delay for the process.
        :param screener: The screener object for the dataset.
        :param pro: The value for the pro interface.
        :param options: The ccxt options.
        :param cancel: The time to cancel the waiting.
        """

        self.options = options or {}

        self.interval = interval

        self.delay = delay or self.DELAY

        self.built = False

        self.pro = pro

        self.signature = ScreenerSignature(
            ticker=self.ticker, source=self.source,
            delay=self.delay, pro=self.pro
        )

        if self.signature not in self.screeners:
            if screener is None:
                self.built = True

                screener = AutoScreener(
                    ticker=self.ticker, source=self.source,
                    delay=self.delay, pro=self.pro,
                    options=self.options
                )
            # end if

            self.screeners[self.signature] = screener
        # end if

        self.screener = self.screeners[self.signature]

        self.market = self.validate_data(data, length=length)

        super().__init__(
            ticker=ticker, source=source,
            location=location, cancel=cancel
        )
    # end __init__

    def validate_data(self, data: Any, length: Optional[int]) -> pd.DataFrame:
        """
        Validates the asset data value.

        :param data: The asset data.
        :param length: The length of the data to add.

        :return: The validates source.
        """

        if not all(
            hasattr(self, name) for name in ["source", "interval"]
        ):
            raise AttributeError(
                "Source and interval attributes must be defined "
                "before attempting to validate the data parameter data."
            )
        # end if

        if (
            (data is None) and
            (
                (length is None) or
                (length == 0) or
                (length is False) or
                (
                    isinstance(length, int) and
                    not (0 < length <= 500)
                )
            )
        ):
            data = pd.DataFrame(
                {column: [] for column in self.COLUMNS},
                index=[]
            )

        elif (data is None) and (isinstance(length, int)):
            if 0 < length <= 500:
                try:
                    exchange = getattr(ccxt, self.source)(self.options)

                    data = self.data_to_dataset(
                        exchange.fetch_ohlcv(
                            symbol=self.ticker,
                            timeframe=self.interval,
                            limit=length
                        )
                    )

                except Exception as e:
                    warnings.warn(str(e))

                    data = pd.DataFrame(
                        {column: [] for column in self.COLUMNS},
                        index=[]
                    )
                # end try

            else:
                raise ValueError(
                    f"Length must be a positive int between "
                    f"1 and 500 when data is not defined, "
                    f"not: {length}."
                )
            # end if
        # end if

        return data
    # end validate_data

    def data_to_dataset(self, data: Iterable[Iterable]) -> pd.DataFrame:
        """
        Adjusts the dataset to an asset Open, High, Low, Close, Bids, Asks, Volume dataset.

        :param data: The data to adjust.

        :return: The asset dataset.
        """

        data = ohlcv_to_dataset(data=data)

        if len(self.screener.market) == 0:
            asks = [np.nan] * len(data)
            bids = [np.nan] * len(data)

        else:
            asks = (
                self.screener.market[AutoScreener.ASKS].iloc
                [-len(data):].values[:]
            )
            bids = (
                self.screener.market[AutoScreener.BIDS].iloc
                [-len(data):].values[:]
            )
        # end if

        data[AutoScreener.ASKS].values[:] = asks
        data[AutoScreener.BIDS].values[:] = bids

        return data[list(self.COLUMNS)]
    # end data_to_dataset

    def dataset_path(
            self, location: Optional[str] = None
    ) -> str:
        """
        Creates the path to the saving file for the screener object.

        :param location: The saving location of the dataset.

        :return: The saving path for the dataset.
        """

        return super().dataset_path(location=location).replace(
            '.csv', f'_{self.interval}.csv'
        )
    # end dataset_path

    def run(
            self,
            save: Optional[bool] = True,
            block: Optional[bool] = False,
            wait: Optional[Union[bool, Number, dt.timedelta, dt.datetime]] = False,
            timeout: Optional[Union[Number, dt.timedelta, dt.datetime]] = None
    ) -> threading.Thread:
        """
        Runs the process of the price screening.

        :param save: The value to save the data.
        :param wait: The value to wait after starting to run the process.
        :param block: The value to block the execution.
        :param timeout: The valur to add a timeout to the process.
        """

        if not self.screener.running:
            self.screener.run(
                wait=True, block=False, timeout=timeout, save=False
            )
        # end if

        return super().run(
            wait=wait, block=block, timeout=timeout, save=save
        )
    # end run

    def update_market(self) -> None:
        """Updates the market data."""

        data = row_to_dataset(self.screener.market, index=-1)

        # noinspection PyBroadException
        try:
            prices = self.validate_data(data=None, length=1)
            prices[AutoScreener.BIDS].values[:] = (
                data[AutoScreener.BIDS].values[:]
            )
            prices[AutoScreener.ASKS].values[:] = (
                data[AutoScreener.ASKS].values[:]
            )
            data = prices

        except Exception as e:
            warnings.warn(str(e))
        # end try

        self.market = pd.concat([self.market, data])
        self.market = self.market[
            ~self.market.index.duplicated(keep='first')
        ]
    # end async_update_market

    def run_loop(self) -> None:
        """Runs the process of the price screening."""

        self.running = True

        delay = interval_to_total_time(self.interval).seconds

        while self.running:
            start = time.time()

            self.update_market()

            end = time.time()

            time.sleep(max([delay - (end - start), 0]))
        # end while
    # end run_loop

    def terminate(self) -> None:
        """Stops the trading process."""

        super().terminate()

        if self.built:
            self.screener.terminate()
        # end if
    # end terminate

    def stop(self) -> None:
        """Stops the screening process."""

        super().stop()

        if self.built:
            self.screener.stop()
        # end if
    # end stop
# end LiveAssetData

Screener = Union[AutoScreener, AutoDataset]

class MultiScreener(BaseModel, AutoDataCollector):
    """
    A class to represent an asset price screener.

    Using this class, you can create a screener object to
    screen the market ask and bid data for a specific asset in
    a specific exchange at real time.

    Parameters:

    - exchanges:
        The data of exchanges and their tickers to screen.

    - interval:
        The interval for the time between data points in the dataset.

    - delay:
        The delay to wait between each data fetching.

    - length:
        An initial dataset length to start with.

    - locaion:
        The saving location for the saved data of the screener.

    - pro:
        The value to use the pro interface.

    - options:
        The ccxt options for the backend screening process.

    - cencel:
        The time to cancel screening process after no new data is fetched.

    >>> from auto_screener.screening import MultiScreener
    >>> from auto_screener.screener import wait_for_initialization
    >>>
    >>> screener = MultiScreener(
    >>>     exchanges={
    >>>         "binance": ["BTC/USDT", "AAVE/EUR"],
    >>>         "bittrex": ["GRT/USD", "BTC/USD"]
    >>>     }
    >>> )
    >>>
    >>> screener.run(wait=True)
    >>>
    >>> while True:
    >>>     screener.wait_for_update(delay=1)
    """

    modifiers = Modifiers(
        excluded=[
            "exchange", "screening_process",
            "timeout_process", "screeners"
        ]
    )

    INTERVAL = "1m"

    DELAY = 1
    CANCEL = 60

    PRO = False

    OPTIONS = {}

    def __init__(
            self,
            exchanges: Dict[str, Iterable[str]],
            delay: Optional[Union[Number, dt.timedelta]] = None,
            interval: Optional[Union[bool, str]] = None,
            length: Optional[Union[int, bool]] = None,
            location: Optional[str] = None,
            pro: Optional[bool] = None,
            options: Optional[Dict[str, Any]] = None,
            cancel: Optional[Union[Number, dt.timedelta]] = None
    ) -> None:
        """
        Defines the class attributes.

        :param interval: The interval of the data to load.
        :param exchanges: The data of exchanges and their tickers.
        :param pro: The value to use the pro interface.
        :param location: The saving location for the data.
        :param delay: The delay between each data fetching request.
        :param length: The length of the data to get in each request.
        :param options: The ccxt options.
        :param cancel: The time it takes to cancel a non-updating screener.
        """

        if interval is True:
            interval = self.INTERVAL

        elif interval is False:
            interval = None
        # end if

        self.options = options or self.OPTIONS

        self.interval = interval
        self.location = location or self.LOCATION

        self.delay = delay or self.DELAY
        self.cancel = cancel or self.CANCEL
        self.length = length

        self.pro = pro or self.PRO

        self.exchanges = self.validate_exchanges(exchanges)

        self.running = False
        self.block = False
        self.saving = False

        self.market: Dict[str, Dict[str, Optional[Screener]]] = {}
        self.invalid: Dict[str, List[str]] = {}
        self.screeners: List[Screener] = []
        self.stopped: List[Screener] = []
        self.loaded: Set[Screener] = set()

        self.saving_process = None
        self.timeout_process = None
    # end Screener

    @staticmethod
    def validate_exchanges(data: Any) -> Dict[str, List[str]]:
        """
        Validates the data.

        :param data: The data to validate.

        :return: The valid data.
        """

        if data is None:
            return {}
        # end if

        try:
            if not isinstance(data, dict):
                raise ValueError
            # end if

            new_data = {}

            for key, values in data.items():
                values = list(values)

                if not (
                    isinstance(key, str) and
                    all(isinstance(value, str) for value in values)
                ):
                    raise ValueError
                # end if

                new_data[key] = values
            # end for

        except (TypeError, ValueError):
            raise ValueError(
                f"Exchanges data must be a dictionary of "
                f"exchange names as keys and iterables of "
                f"ticker names as values, not {data}."
            )
        # end try

        return new_data
    # end validate_data

    def create_screener(
            self,
            container: Dict[str, Optional[Screener]],
            ticker: str,
            source: str
    ) -> None:
        """
        Creates the screener and inserts it into the container.

        :param container: The container to contain the new screener.
        :param ticker: The ticker of the screener.
        :param source: The source of the data.
        """

        try:
            if isinstance(self.interval, str):
                container[ticker] = AutoDataset(
                    ticker=ticker, source=source, options=self.options,
                    interval=self.interval, pro=self.pro, delay=self.delay
                )

            else:
                container[ticker] = AutoScreener(
                    ticker=ticker, source=source, options=self.options,
                    pro=self.pro, delay=self.delay
                )
            # end if

        except ValueError:
            container[ticker] = None

            self.invalid.setdefault(source, []).append(ticker)
        # end try
    # end create_screener

    def create_screeners(
            self,
            container: Dict[str, Optional[Screener]],
            tickers: Iterable[str],
            source: str
    ) -> None:
        """
        Creates the screener and inserts it into the container.

        :param container: The container to contain the new screener.
        :param tickers: The ticker of the screener.
        :param source: The source of the data.
        """

        for ticker in tickers:
            threading.Thread(
                target=self.create_screener,
                kwargs=dict(
                    container=container,
                    ticker=ticker, source=source
                )
            ).start()
        # end for
    # end create_screeners

    def configure_screener_dataset(
            self,
            screener: Screener,
            location: Optional[str] = None,
            length: Optional[int] = None
    ) -> None:
        """
        Configures the dataset of the screener.

        :param screener: The screener object to configure the dataset for.
        :param location: The saving or loading path for the dataset.
        :param length: The length of the dataset to fetch.
        """

        path = screener.dataset_path(location=location)

        if os.path.exists(path):
            try:
                self.load_dataset(screener=screener)

            except Exception as e:
                warnings.warn(str(e))
            # end try

        else:
            if isinstance(screener, AutoDataset):
                screener.market = screener.validate_data(
                    data=None, length=length
                )
            # end if

            if len(screener.market) > 0:
                self.save_dataset(screener=screener)
            # end if
        # end if
    # end configure_screener_dataset

    def wait_for_initialization(
            self,
            delay: Optional[Union[Number, dt.timedelta]] = None,
            once: Optional[bool] = False,
            stop: Optional[Union[bool, int]] = False,
            cancel: Optional[Union[Number, dt.timedelta, dt.datetime]] = None
    ) -> WaitingState:
        """
        Waits for all the screeners to update.

        :param delay: The delay for the waiting.
        :param once: The value to get data only once.
        :param stop: The value to stop the screener objects.
        :param cancel: The time to cancel the waiting.

        :returns: The total delay.
        """

        return wait_for_dynamic_initialization(
            self.screeners, delay=delay, once=once,
            stop=stop, cancel=cancel
        )
    # end wait_for_initialization

    def wait_for_update(
            self,
            delay: Optional[Union[Number, dt.timedelta]] = None,
            once: Optional[bool] = False,
            stop: Optional[Union[bool, int]] = False,
            cancel: Optional[Union[Number, dt.timedelta, dt.datetime]] = None
    ) -> WaitingState:
        """
        Waits for all the screeners to update.

        :param delay: The delay for the waiting.
        :param once: The value to get data only once.
        :param stop: The value to stop the screener objects.
        :param cancel: The time to cancel the waiting.

        :returns: The total delay.
        """

        return wait_for_dynamic_update(
            self.screeners, delay=delay, once=once,
            stop=stop, cancel=cancel
        )
    # end wait_for_update

    def initialize_screeners(self) -> None:
        """Initializes the screeners."""

        self.market.clear()

        for exchange, tickers in self.exchanges.items():
            self.market[exchange] = {}

            threading.Thread(
                target=self.create_screeners,
                kwargs=dict(
                    container=self.market[exchange],
                    tickers=tickers, source=exchange
                )
            ).start()
        # end for

        while (
            sum(len(screeners) for screeners in self.market.values()) <
            sum(len(tickers) for tickers in self.exchanges.values())
        ):
            time.sleep(3)
        # end while

        self.screeners.clear()

        for exchange in self.market.values():
            for ticker, screener in exchange.copy().items():
                if isinstance(screener, (AutoScreener, AutoDataset)):
                    self.screeners.append(screener)

                else:
                    exchange.pop(ticker)
                # end if
            # end for
        # end for
    # end initialize_screeners

    def prepare_screeners(self) -> None:
        """Initializes the screeners."""

        if not (self.market and self.screeners):
            self.initialize_screeners()
        # end if

        for screener in self.screeners:
            if screener.running:
                continue
            # end if

            threading.Thread(
                target=self.configure_screener_dataset,
                kwargs=dict(
                    screener=screener,
                    location=self.location,
                    length=self.length
                )
            ).start()
        # end for
    # end prepare_screeners

    async def async_get_market(self) -> Dict[str, Dict[str, Dict[str, Number]]]:
        """Gets the market data."""

        market = {exchange: {} for exchange in self.exchanges}

        for screener in self.screeners:
            market[screener.source][screener.ticker] = (
                await screener.async_get_market()
            )
        # end for

        return market
    # end async_get_market

    async def async_update_market(self) -> None:
        """Updates the market data."""

        for screener in self.screeners:
            await screener.async_update_market()
        # end for
    # end async_update_market

    def update_market(self) -> None:
        """Updates the market data."""

        asyncio.run(self.async_update_market())
    # end update_market

    def get_market(self) -> Dict[str, Dict[str, Dict[str, Number]]]:
        """Gets the market data."""

        return asyncio.run(self.async_get_market())
    # end get_market

    def start_screeners(
            self,
            save: Optional[bool] = True,
            wait: Optional[Union[bool, Number, dt.timedelta, dt.datetime]] = False,
            timeout: Optional[Union[Number, dt.timedelta, dt.datetime]] = None
    ) -> None:
        """
        Runs the data collection.

        :param save: The value to save the data.
        :param timeout: The valur to add a timeout to the process.
        :param wait: The value to wait after starting to run the process.
        """

        self.prepare_screeners()

        for screener in self.screeners:
            threading.Thread(
                target=screener.run,
                kwargs=dict(
                    timeout=timeout, wait=False,
                    block=False, save=save
                )
            ).start()
        # end for

        if isinstance(wait, dt.datetime):
            wait = wait - dt.datetime.now()
        # end if

        if isinstance(wait, dt.timedelta):
            wait = wait.total_seconds()
        # end if

        if isinstance(wait, bool) and wait:
            self.wait_for_initialization()

        elif isinstance(wait, (int, float)):
            time.sleep(wait)
        # end if
    # end start_screeners

    def stop(self) -> None:
        """Stops the screening process."""

        self.running = False
        self.saving = False

        if isinstance(self.screening_process, threading.Thread):
            terminate_thread(self.screening_process)
        # end if

        if isinstance(self.saving_process, threading.Thread):
            terminate_thread(self.saving_process)
        # end if

        if isinstance(self.timeout_process, threading.Thread):
            terminate_thread(self.timeout_process)
        # end if
    # end stop

    def terminate(self) -> None:
        """Stops the screening process."""

        self.stop()

        for screener in self.screeners:
            screener.terminate()
        # end for
    # end terminate

    def blocking(self) -> bool:
        """
        returns the value of the process being blocked.

        :return: The value.
        """

        return self.block
    # end blocking

    def save_dataset(self, screener: Screener) -> None:
        """
        Saves the data of the screener.

        :param screener: The screener object to save its data.
        """

        screener.save_dataset()

        if screener in self.loaded:
            self.loaded.remove(screener)
        # end if
    # end save_dataset

    def load_dataset(self, screener: Screener) -> None:
        """
        Saves the data of the screener.

        :param screener: The screener object to save its data.
        """

        screener.load_dataset()

        self.loaded.add(screener)
    # end save_dataset

    def handle(
            self,
            screener: Screener,
            cancel: Optional[Union[int, dt.timedelta]] = None
    ) -> None:
        """
        Handles the screener during the screening loop.

        :param screener: The screener object.
        :param cancel: The time it takes to cancel a non-updating screener.
        """

        if cancel is None:
            cancel = self.cancel
        # end if

        if len(screener.market) == 0:
            return
        # end if

        if isinstance(cancel, dt.timedelta):
            cancel = cancel.total_seconds()
        # end if

        cancel += (
            interval_to_total_time(screener.interval).seconds
            if isinstance(screener, AutoDataset) else 0
        )

        if (
            (screener not in self.loaded) and
            (dt.datetime.now() - screener.market.index[-1]).seconds >= cancel
        ):
            screener.terminate()

            self.stopped.append(screener)
            self.screeners.remove(screener)

        elif self.saving:
            self.save_dataset(screener=screener)
        # end if
    # end handle

    def saving_loop(self) -> None:
        """Runs the process of the price screening."""

        self.running = True

        while self.running:
            for screener in self.screeners.copy():
                self.handle(screener=screener)
            # end for

            delay = self.delay

            if isinstance(self.delay, dt.timedelta):
                delay = delay.total_seconds()
            # end if

            time.sleep(delay or 1)
        # end while
    # end run_loop

    def run(
            self,
            save: Optional[bool] = True,
            block: Optional[bool] = False,
            wait: Optional[Union[bool, Number, dt.timedelta, dt.datetime]] = False,
            timeout: Optional[Union[Number, dt.timedelta, dt.datetime]] = None
    ) -> Optional[threading.Thread]:
        """
        Runs the process of the price screening.

        :param save: The value to save the data.
        :param block: The value to block the execution.
        :param timeout: The valur to add a timeout to the process.
        :param wait: The value to wait after starting to run the process.
        """

        self.start_screeners(timeout=timeout, wait=wait, save=save)

        return super().run(
            save=False, block=block, wait=wait, timeout=timeout
        )
    # end run
# end Screener

def live_screeners(
        screeners: Iterable[Union[Screener, MultiScreener]]
) -> List[Union[Screener, MultiScreener]]:
    """
    Returns a list of all the live screeners.

    :param screeners: The screeners to search from.

    :return: A list the live screeners.
    """

    return [
        screener for screener in screeners
        if (
            screener.running and (
                isinstance(screener, MultiScreener) or
                len(screener.market) > 0
            )
        )
    ]
# end live_screeners