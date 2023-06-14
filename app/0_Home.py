import streamlit as st

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go

import time
import requests

st.set_page_config(
    layout="wide"
)

### Load df_1d from csv

df_1d = pd.read_csv('data/raw_data/BTCUSDT_daily.csv')
df_1d["timestamp"] = pd.to_datetime(df_1d["timestamp"])
df_1d["timestamp"] = df_1d["timestamp"] - pd.Timedelta(hours=3)
df_1d["timestamp"] = df_1d["timestamp"].dt.floor("D")
df_1d = df_1d[df_1d["timestamp"] > "2023-01-01"]

df_1w = pd.read_csv("app/assets/data/BTC-USD_1W.csv")
df_1w = df_1w.drop(columns=["Adj Close", "Volume"])
df_1w["Date"] = pd.to_datetime(df_1w["Date"])
df_1w = df_1w[df_1w["Date"] > "2022-12-25"]

### Tickers

# Create dictionary to hold values
currencies = {
    'BTCUSDT' : [],
    'ETHUSDT': [],
    'DOGEUSDT': [],
    'BNBUSDT': [],
    'ADAUSDT': [],
    'XRPUSDT': []
}

URL = "https://api.binance.com/api/v3/ticker/price"

placeholder = st.empty()

for s in range(300):

    with placeholder.container():
    # Do api calls here

        for k in currencies.keys():

            params = {"symbol": k}
            response = requests.get(URL, params=params).json()['price']
            currencies[k].append(round(float(response), 3))

            if len(currencies[k]) > 2:
                del currencies[k][0]

        # Create diffs here
        if len(currencies['BTCUSDT']) > 1:

            btc_diff = (currencies['BTCUSDT'][-1] / currencies["BTCUSDT"][-2] - 1) * 100
            eth_diff = (currencies['ETHUSDT'][-1] / currencies["ETHUSDT"][-2] - 1) * 100
            doge_diff = (currencies['DOGEUSDT'][-1] / currencies["DOGEUSDT"][-2] - 1) * 100
            bnb_diff = (currencies['BNBUSDT'][-1] / currencies["BNBUSDT"][-2] - 1) * 100
            ada_diff = (currencies['ADAUSDT'][-1] / currencies["ADAUSDT"][-2] - 1) * 100
            xrp_diff = (currencies['XRPUSDT'][-1] / currencies["XRPUSDT"][-2] - 1) * 100
        else:
            btc_diff = 0
            eth_diff = 0
            doge_diff = 0
            bnb_diff = 0
            ada_diff = 0
            xrp_diff = 0

        # Create columns
        tick1, tick2, tick3, tick4, tick5, tick6 = st.columns(6)


        with tick1:
            st.metric("BTC", currencies["BTCUSDT"][-1], f"{btc_diff: 0.3f} %")

        with tick2:
            st.metric("ETH", currencies["ETHUSDT"][-1], f"{eth_diff: 0.3f} %")

        with tick3:
            st.metric("DOGE", currencies["DOGEUSDT"][-1], f"{doge_diff: 0.3f} %")

        with tick4:
            st.metric("BNB", currencies["BNBUSDT"][-1], f"{bnb_diff: 0.3f} %")

        with tick5:
            st.metric("ADA", currencies["ADAUSDT"][-1], f"{ada_diff: 0.3f} %")

        with tick6:
            st.metric("XRP", currencies["XRPUSDT"][-1], f"{xrp_diff: 0.3f} %")


        ### Below Tickers

        ###
        st.title("ASSIST TRADER")
        st.subheader("Building models to predict the next period of Cryptocurrency market for Traders")

        ### Candlestick plot

        # Create figure
        fig = go.Figure(
            data=[
                go.Candlestick(
                    x=df_1w['Date'],
                    open=df_1w['Open'],
                    high=df_1w['High'],
                    low=df_1w['Low'],
                    close=df_1w['Close']
                ),
                go.Scatter(
                    x=df_1d["timestamp"],
                    y=(df_1d["close"] + df_1d['open']) / 2,
                    mode="lines",
                    marker= {"color":"blue"}
                )
            ])

        # Update fig params
        fig.update_layout(
            title="Bitcoin - USDT",
            width=1000,
            height=600,
            xaxis = {
                "title": "Time",
                "tickmode": "array",
                "tickvals": df_1w["Date"],
                "range": ["2023-01-01", "2023-06-01"],
                "rangeslider_visible": False
            },
            yaxis = {
                "title": "Close Price (USDT)",
                # "range": [10_000, 35_000]
            },
            showlegend=False,
            sliders=[],
            # display
        )

        # Plot
        st.plotly_chart(fig, use_container_width=True)

        # Ticker refresh timer
        time.sleep(30)




st.write('does this work ouside the loop?') # no
