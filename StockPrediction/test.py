# Raw Package
import numpy as np
import pandas as pd
import yfinance as yf
import datetime as dt 
import plotly.graph_objs as go 
import time  # to simulate a real time data, time loop
import plotly.express as px  # interactive charts
import streamlit as st 

STOCK_TICKER = 'AMD'
intervalOptions = ["1m", "2m", "5m", "15m", "30m", "60m", "90m", "1h", "1d", "5d", "1wk", "1mo", "3mo"] 
# Override Yahoo Finance 
yf.pdr_override()

# Retrieve stock information from yfinance API
stock = yf.Ticker(STOCK_TICKER)

# Retrieve stock data frame (df) from yfinance API at an interval of 1m 
df = yf.download(tickers=STOCK_TICKER,period='1d',interval='1m')

# Declare plotly figure (go)
fig=go.Figure()

fig.add_trace(go.Candlestick(x=df.index,
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'], name = 'market data'))

# Customize the layout
fig.update_layout(
    title='Candlestick Chart',
    xaxis_title='Date',
    yaxis_title='Price',
    xaxis_rangeslider_visible=True
)


# fig.update_layout(
#     title= str(STOCK_TICKER)+' Live Share Price:',
#     yaxis_title='Stock Price (USD per Shares)')               

# fig.update_xaxes(
#     rangeslider_visible=True,
#     rangeselector=dict(
#         buttons=list([
#             dict(count=15, label="15m", step="minute", stepmode="backward"),
#             dict(count=45, label="45m", step="minute", stepmode="backward"),
#             dict(count=1, label="HTD", step="hour", stepmode="todate"),
#             dict(count=3, label="3h", step="hour", stepmode="backward"),
#             dict(step="all")
#         ])
#     )
# )

# fig.show()


st.set_page_config(
    page_title=f"IA Trader",
    layout="wide",
)


# dashboard title
st.title(f"{STOCK_TICKER} Live Share Price")

# Interval selection for the stock data
interval_filter = st.selectbox("Select a time interval:", intervalOptions, key="interval")

# creating a single-element container
placeholder = st.empty()

with placeholder.container():
    
    # create three columns
    kpi1, kpi2 = st.columns(2)

    # fill in those three columns with respective metrics or KPIs
    kpi1.metric(
        label="Actual price 💲",
        value=round(df['Close'][-1], 3),
    )
    
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("### Detailed Data View")
    st.dataframe(df, use_container_width=True)
    time.sleep(1)

"""
TODO: use data to display it in real time as a test
"""