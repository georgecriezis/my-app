import streamlit as st
import pandas as pd
import yfinance as yf

st.title("Commodity Correlation Dashboard")
st.write("This dashboard displays the correlation between different commodities. Select a commodity to see its correlation with others.")

tickers = {
    "Crude Oil": "CL=F",
    "Natural Gas": "NG=F",
    "Gold": "GC=F",
    "Silver": "SI=F",
    "Corn": "ZC=F",
    "Wheat": "ZW=F"
}

asset1 = st.selectbox("Pick the first commodity:", list(tickers.keys()), index=0)
asset2 = st.selectbox("Pick the second commodity:", list(tickers.keys()), index=1)

if asset1 == asset2:
    st.warning("Please choose two different commodities.")
else:
    data1 = yf.download(tickers[asset1], period="12mo", progress=False, auto_adjust=True)["Close"]
    data2 = yf.download(tickers[asset2], period="12mo", progress=False, auto_adjust=True)["Close"]

    comparison_table = pd.concat([data1, data2], axis=1)
    comparison_table.columns = [asset1, asset2]
    comparison_table = comparison_table.dropna()

    score = comparison_table[asset1].corr(comparison_table[asset2])

    st.subheader("Correlation Score")
    st.write(f"Correlation between {asset1} and {asset2} is: {score:.2f}")

    st.line_chart(comparison_table)