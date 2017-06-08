import numpy as np  # array operations
from pandas_datareader import data as web  # data retrieval
import seaborn as sns
sns.set()  # nicer plotting style


AAPL = web.DataReader('AAPL', data_source='google')
type(AAPL)
AAPL.info()  # meta information
AAPL.tail()  # final five rows
AAPL['Close'].head()  # first five rows of single column
AAPL[['Open', 'Close']].tail()  # last five rows of 2 columns
AAPL.loc['2016-04-05']  # single row via index value
AAPL.iloc[:2]  # two rows via index numbers
AAPL['Close'].plot(figsize=(10, 6))

# fully vectorized operation for log return calculation
rets = np.log(AAPL['Close'] / AAPL['Close'].shift(1))
rets.hist(figsize=(10, 6), bins=35)

# fully vectorized calculation of 50 days moving average/trend
AAPL['MA50'] = AAPL['Close'].rolling(window=50, center=False).mean()
AAPL[['Close', 'MA50']].plot(figsize=(10, 6))

# fully vectorized calculation of 50 days moving standard diviation/volatile
AAPL['MSD50'] = AAPL['Close'].rolling(window=50, center=False).std()
AAPL['MSD50'].plot(figsize=(10, 6))

# fully vectorized calculation of 50 days moving max
AAPL['MMX50'] = AAPL['Close'].rolling(window=50, center=False).max()
AAPL['MMX50'].plot(figsize=(10, 6))


# pandas DataReader documentation: https://pandas-datareader.readthedocs.io/en/latest/
# Visualization: http://pandas.pydata.org/pandas-docs/stable/visualization.html
# Computational tools: http://pandas.pydata.org/pandas-docs/stable/computation.html
