from matplotlib import ticker
import streamlit as st
import pandas as pd
import yfinance as yf # to pull market data

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

# The Inputs (select two different ones)
asset1 = st.selectbox("Pick the first commodity:", list(tickers.keys()), index=0) #index starts dropdown with first item
asset2 = st.selectbox("Pick the second commodity:", list(tickers.keys()), index=1)

# Get data
# Tells yahoo finance to pull last x months of price data
data1 = yf.download(ticker[asset1], period="12mo")["Close"]
data2 = yf.download(ticker[asset2], period="12mo")["Close"]

# Combine data to compare it
#Put both price lisrs into one table

comparison_table = pd.concat([data1,data2], axis=1) #axis 1 refers to columns

#rename columns so table is easy to read
comparison_table.columns = [asset1, asset2]

# this compares two columns and gives us a score
# (1.00 means they move perfectly together, -1.00 means they move in opposite directions)

score = comparison_table[asset1].corr(comparison_table[asset2])

#Results
st.subheader('Correlation Score')

st.write(f'Correlation between {asset1} and {asset2} is: {score:.2f}') #:.2f formats the score to 2 decimal places

#draw the line chart using our table
st.line_chart(comparison_table)