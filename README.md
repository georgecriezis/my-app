# my-app
# Commodity Correlation Dashboard

## Student Name
# George Criezis
 
## App Description
# This app will help users compare two commodity futures and see how closely they move together over time. It will show the relationship between the two markets with a simple chart and correlation score.
 
## Intended Users
# This app is intended for students, beginner traders, and anyone interested in commodity markets. It is especially useful for people who want a simple way to study market relationships.
 
## Planned Features
# Choose two commodity futures or related stocks to compare.
# View a chart of both prices over time.
# See the correlation between the two commodities/stocks.
# Show simple market metrics like daily change or volatility.

# Added Features for Assignment 2:
- # Real-Time Data Integration: Uses the yfinance library to fetch live historical closing prices from Yahoo Finance.

- # Interactive Selection: Two dynamic st.selectbox widgets allow users to pair any two assets from a comprehensive database.

- # Cross-Asset Database: Includes Commodity Futures (Oil, Gold, Corn), Equity Indexes (SPY, QQQ, IWM), and Mining/Energy Stocks (Exxon, Newmont).

- # Automated Correlation Math: Real-time calculation of the correlation score over a 12-month trailing period.

- # Visual Data Comparison: Dynamic line charts that update instantly based on user selection.

- # Data Cleaning: Automated handling of missing market data (weekends/holidays) using pandas.

# Planned Features for Final Version
- # Add a dynamic summary that explains the strength and direction of the relationship based on the correlation coefficient, ranging from -1.0 to +1.0.
- # A measure to show how volitile each ticker is
- # Show the raw data if the user actually wants to see the actual numbers behind the chart. I will hide this raw data table behind a checkbox, so the app doesn't feel cluttered
- # Add a Data Normalization feature as it can be hard to compare drastically different prices between different assets.

# Challenges with Assignment 2
- # I had to search up how to incorporate real-time data to support my charts.
- # To support my project, I had to research some more math-based uses python can offer as well as what code to write to format the columns and rows such as index=0 and index=1.

# Overall, my project is drastically improving and I expect the same outcome for the final version
