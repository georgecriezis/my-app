import yfinance as yf
import pandas as pd

# 1. Define the tickers (APD and 10-Year Treasury Yield)
tickers = ["APD", "^TNX"]

# 2. Download the last 3 years of data
# We specifically pull the 'Close' prices only
data = yf.download(tickers, period="3y")['Close']

# 3. Rename columns for clarity
# Note: ^TNX represents the interest rate percentage (e.g., 4.2 = 4.2%)
data.columns = ['APD_Price', '10Y_Treasury_Yield']

# 4. Save directly to an Excel file
data.to_excel("APD_and_Treasury_3Year_Data.xlsx")

print("Success! Your Excel file 'APD_and_Treasury_3Year_Data.xlsx' has been created.")