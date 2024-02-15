import yfinance as yf

tickers = yf.Tickers('msft aapl goog')

# access each ticker using (example)
a = tickers.tickers['MSFT'].info
b = tickers.tickers['AAPL'].history(period="1mo")
c = tickers.tickers['GOOG'].actions

print(c)