# ₿ Bitcoin Price Dashboard

This is a simple interactive web application built with Streamlit to display and analyze Bitcoin (BTC-USD) price data.

## Features

-   Fetches data from Yahoo Finance using the `yfinance` library.
-   Displays the raw price data in an interactive table.
-   Visualizes the data using a Plotly Candlestick chart.
-   Provides an option to calculate the average closing price for the selected period.

## How to Run

1.  **Install the required libraries:**
    ```bash
    pip install streamlit pandas yfinance plotly
    ```

2.  **Run the Streamlit application from your terminal:**
    ```bash
    streamlit run bitcoin_app.py
    ```