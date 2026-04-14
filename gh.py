import streamlit as st
import pandas as pd
import yfinance as yf
import numpy as np

st.title("Commodity Correlation & 'What-If' Simulator")

tickers = {
    "S&P 500 (ETF)": "SPY",
    "Gold (Futures)": "GC=F",
    "Silver (Futures)": "SI=F",
    "Crude Oil": "CL=F",
    "Natural Gas": "NG=F",
    "Bitcoin": "BTC-USD"
}

asset1 = st.selectbox("Select your asset:", list(tickers.keys()), index=1)
investment = st.number_input("Investment Amount ($):", value=1000)

# 1. Fetch Data for selected asset AND the Benchmark (S&P 500)
data = yf.download([tickers[asset1], "^GSPC"], period="12mo", progress=False)["Close"]
data = data.dropna()

# 2. Calculate Returns
# Formula: (Current Price / Starting Price) * Investment
start_price_asset = data[tickers[asset1]].iloc[0]
end_price_asset = data[tickers[asset1]].iloc[-1]
asset_final_val = (end_price_asset / start_price_asset) * investment

start_price_bench = data["^GSPC"].iloc[0]
end_price_bench = data["^GSPC"].iloc[-1]
bench_final_val = (end_price_bench / start_price_bench) * investment

# 3. Display Comparison
st.subheader(f"What if you invested ${investment:,} a year ago?")

col1, col2 = st.columns(2)

with col1:
    st.metric(label=asset1, value=f"${asset_final_val:,.2f}", 
              delta=f"{(asset_final_val - investment)/investment:.1%}")

with col2:
    # Benchmark Toggle logic
    show_bench = st.toggle("Compare to S&P 500", value=True)
    if show_bench:
        st.metric(label="S&P 500 (Benchmark)", value=f"${bench_final_val:,.2f}", 
                  delta=f"{(bench_final_val - investment)/investment:.1%}")

# 4. Normalized Performance Chart
st.write("### Relative Performance (Growth of $1)")
normalized_data = data / data.iloc[0]
st.line_chart(normalized_data)