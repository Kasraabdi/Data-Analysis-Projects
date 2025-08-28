import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.graph_objects as go

st.title("Bitcoin Price Dashboard")

st.markdown("This app fetches and displays Bitcoin (BTC-USD) price data for the year 2023.")
try:
    btc_data = yf.download('BTC-USD', start='2023-01-01', end='2024-01-01')
    data_loaded = True
except Exception as e:
    st.error(f"Error downloading data: {e}")
    data_loaded = False

if data_loaded:
    if "show_data" not in st.session_state:
        st.session_state.show_data = False

    if st.button("Show Bitcoin Data & Chart"):
        st.session_state.show_data = True

    if st.session_state.show_data:
        st.subheader("Bitcoin Raw Data (2023)")
        st.dataframe(btc_data)

        st.subheader("Bitcoin Candlestick Chart")
        fig = go.Figure(data=[go.Candlestick(
            x=btc_data.index,
            open=btc_data["Open"],
            high=btc_data["High"],
            low=btc_data["Low"],
            close=btc_data["Close"]
        )])

        fig.update_layout(
            title='Bitcoin Price (2023)',
            yaxis_title='Price (USD)',
            xaxis_title='Date'
        )

        st.plotly_chart(fig)

        if st.button("Calculate Average Closing Price"):
            avg_price = btc_data["Close"].mean()
            st.success(f"The average closing price in this period was: ${avg_price:,.2f}")
























