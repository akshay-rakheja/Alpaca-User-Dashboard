from alpaca.data.timeframe import TimeFrame
from alpaca.data.requests import CryptoBarsRequest
from alpaca.data.historical import CryptoHistoricalDataClient
from alpaca.data.historical import CryptoHistoricalDataClient
from alpaca.data.requests import CryptoBarsRequest
from alpaca.data.timeframe import TimeFrame
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce
import streamlit as st
import config

# no keys required for crypto data
client = CryptoHistoricalDataClient()
# Alpaca Trading Client
trading_client = TradingClient(
    config.APCA_API_KEY_ID, config.APCA_API_SECRET_KEY, paper=True)


# request_params = CryptoBarsRequest(
#     symbol_or_symbols=["BTC/USD", "ETH/USD"],
#     timeframe=TimeFrame.Day,
#     start="2022-07-01"
# )

st.title("Alpaca Trading Dashboard")


@st.cache
def get_positions():
    positions = trading_client.get_all_positions()
    st.table(positions)
    return positions

# bars = client.get_crypto_bars(request_params)
