import streamlit as st
import pandas as pd
import yfinance as yf

def main():

    st.title("Commodity Correlation Dashboard")
    st.write("This dashboard displays the correlation between different commodities. Select a commodity to see its correlation with others.")

    tickers = {
        #  INDEXES & ETFs 
        "S&P 500 (E-mini)": "ES=F",
        "Nasdaq 100 (E-mini)": "NQ=F",
        "Dow Jones (E-mini)": "YM=F",
        "Russell 2000": "RTY=F",
        "S&P 500 (SPY)": "SPY",
        "Nasdaq 100 (QQQ)": "QQQ",
        "Russell 2000 (IWM)": "IWM",

        # METALS & MINERS 
        "Gold (Futures)": "GC=F",
        "Silver (Futures)": "SI=F",
        "Copper (Futures)": "HG=F",
        "Gold ETF (GLD)": "GLD",
        "Newmont Gold Mining": "NEM",
        "Barrick Gold": "GOLD",
        "Freeport-McMoRan (Copper)": "FCX",
        "Southern Copper": "SCCO",
        
        # ENERGY & OIL STOCKS
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

# Widget 3: Lookback Period
        timeframe = st.sidebar.radio("Select Lookback Period:", 
                                 ("6mo", "1y", "2y", "5y"), index=1)

        comparison_table = pd.concat([data1, data2], axis=1)
        comparison_table.columns = [asset1, asset2]
        comparison_table = comparison_table.dropna()

        score = comparison_table[asset1].corr(comparison_table[asset2])

        st.subheader("Correlation Score")
        st.write(f"Correlation between {asset1} and {asset2} is: {score:.2f}")

        st.line_chart(comparison_table)

        # Normalize to start at 100
        normalized_df = (comparison_table / comparison_table.iloc[0]) * 100
        st.subheader("Price Comparison (Base 100)")
        st.line_chart(normalized_df)

    # To help understand charts
    with st.expander("What am I looking at?"):
        st.write("""
            This dashboard tracks the statistical relationship between assets. 
            A score of 1.0 means they move perfectly together, 
            while -1.0 means they move in opposite directions.
                
            The Price Comparison chart normalizes both assets to a base of 100 at the start of the period,
            allowing you to see how they have performed relative to each other over time.
        """)

main()