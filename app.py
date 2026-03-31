import streamlit as st
import pandas as pd

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

df = pd.DataFrame(list(tickers.items()), columns=["Commodity", "Ticker"])
st.dataframe(df)