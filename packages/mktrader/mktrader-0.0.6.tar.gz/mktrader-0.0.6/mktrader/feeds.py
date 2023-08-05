from .models import DataFeed, Candle
from .logger import logger
from typing import Optional, List
from datetime import datetime, timedelta
import requests
import websocket
import json


class Alpaca_Historical_Bars(DataFeed):
    ALPACA_DATA_API_URL = "https://data.alpaca.markets"

    def __init__(self, engine, api_key: str, api_secret: str, sip: Optional[bool] = False):
        super().__init__(engine)
        self.api_key = api_key
        self.api_secret = api_secret
        self.sip = sip

    def get_candles(self, minute_catch_up: Optional[datetime] = None) -> List[Candle]:
        time_period = self.engine.strategy.time_period
        time_int = self.engine.strategy.time_int

        if minute_catch_up is not None:
            time_int = 1
            time_period = "min"

        if time_period == "hour":
            time_period = "Hour"
        if time_period == "min":
            time_period = "Min"
        if self.engine.asset.asset_class == "us_equity":
            endpoint = f"/v2/stocks/{self.engine.asset.symbol}/bars?timeframe={time_int}{time_period}"
            logger.debug(endpoint)
        elif self.engine.asset.asset_class == "crypto":
            endpoint = f"/v1beta3/crypto/us/bars?symbols={self.engine.asset.symbol}&timeframe={time_int}{time_period}"
            logger.debug(endpoint)
        if self.engine.strategy.limit:
            endpoint = f"{endpoint}&limit={self.engine.strategy.limit}"
            logger.debug(endpoint)
            
        url = self.ALPACA_DATA_API_URL + endpoint
        logger.debug(f"URL = {url}")
        headers = {
            'APCA-API-KEY-ID': self.api_key,
            'APCA-API-SECRET-KEY': self.api_secret
        }
        logger.debug(f"fetching candles from {url}")
        response = requests.get(url=url, headers=headers)
        json_response = response.json()
        if json_response["bars"] is None:
            logger.debug(json_response)
            logger.error("No bars found (weekend?)..retrying with start time as limit 1000 prior periods")
            if time_period == "Min":
                start = (datetime.utcnow() - timedelta(minutes=1000)).strftime("%Y-%m-%dT%H:%M:%SZ")
            elif time_period == "Hour":
                start = (datetime.utcnow() - timedelta(hours=1000)).strftime("%Y-%m-%dT%H:%M:%SZ")
            url = f"{url}&start={start}"
            logger.debug(f"URL = {url}")
            logger.debug(f"fetching candles from {url}")
            response = requests.get(url=url, headers=headers)
            json_response = response.json()
            if json_response["bars"] is None:
                print("no bars after 1000 latest pulled.. skipping")
        candles = []


        if self.engine.asset.asset_class == "us_equity":
            bars_list = json_response["bars"]
        elif self.engine.asset.asset_class == "crypto":
            bars_list = json_response["bars"][self.engine.asset.symbol]
        if json_response["bars"]:
            for bar in bars_list:
                candle = Candle(
                    ticker=self.engine.asset.symbol,
                    date=datetime.strptime(bar['t'], "%Y-%m-%dT%H:%M:%SZ"),
                    open=bar["o"],
                    high=bar["h"],
                    low=bar["l"],
                    close=bar["c"],
                    volume=bar["v"]
                )
                candles.append(candle)

        if minute_catch_up is not None:
            print(f"MINUTE CATCH UP: {minute_catch_up}")
            minute_candles = [candle for candle in candles if candle.date >= minute_catch_up]
            for minute_candle in minute_candles:
                if minute_candle.date.minute == datetime.utcnow().minute:
                    print(f"IN PROCESS, REMOVING: {minute_candle}")
                    del minute_candles[minute_candles.index(minute_candle)]
            return minute_candles
        else:
            return candles


class Alpaca_Live_Bars(DataFeed):
    ALPACA_STREAM_API_URL_IEX = "wss://stream.data.alpaca.markets/v2/iex"
    ALPACA_STREAM_API_URL_SIP = "wss://stream.data.alpaca.markets/v2/sip"
    ALPACA_STREAM_API_URL_CRYPTO = "wss://stream.data.alpaca.markets/v1beta2/crypto"
    ALPACA_DATA_API_URL = "https://data.alpaca.markets"

    def __init__(self, engine, api_key: str, api_secret: str, sip: Optional[bool] = False):
        super().__init__(engine)
        self.api_key = api_key
        self.api_secret = api_secret
        self.sip = sip

        if self.sip is True:
            self.api_stream_url = self.ALPACA_STREAM_API_URL_SIP
        else:
            self.api_stream_url = self.ALPACA_STREAM_API_URL_IEX

    def get_candles(self, minute_catch_up: Optional[datetime] = None):
        return Alpaca_Historical_Bars.get_candles(self, minute_catch_up)

    def get_live_candles(self) -> List[Candle]:
        if self.engine.asset.asset_class == "us_equity":
            socket_url = self.api_stream_url
        elif self.engine.asset.asset_class == "crypto":
            socket_url = self.ALPACA_STREAM_API_URL_CRYPTO
        logger.debug(f"SOCKET URL: {socket_url}")

        def on_open(ws):
            auth_message = {"action": "auth", "key": self.api_key, "secret": self.api_secret}
            ws.send(json.dumps(auth_message))
            subscribe_message = {"action": "subscribe", "bars": [self.engine.asset.symbol]}
            ws.send(json.dumps(subscribe_message))

        def on_message(ws, message):
            json_data = json.loads(message)
            for item in json_data:
                if item['T'] == 'b':
                    candle = Candle(
                        ticker=item['S'],
                        date=datetime.strptime(item['t'], "%Y-%m-%dT%H:%M:%SZ"),
                        open=float(item['o']),
                        high=float(item['h']),
                        low=float(item['l']),
                        close=float(item['c']),
                        volume=float(item['v'])
                    )
                    logger.debug(candle)
                    self.engine.on_candle(candle)
                else:
                    logger.info(item)

        def on_close(ws):
            logger.info("Websocket Connection Closed..")


        # Connect to the WebSocket
        ws = websocket.WebSocketApp(socket_url, on_open=on_open, on_message=on_message, on_close=on_close)
        ws.run_forever()
