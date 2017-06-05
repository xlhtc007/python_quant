import numpy as np  # array operations
import pandas as pd  # time series management
from pandas_datareader import data as web  # data retrieval
import seaborn as sns;
sns.set()  # nicer plotting style


AAPL = web.DataReader('AAPL', data_source='yahoo')
type(AAPL)
AAPL.info()  # meta information
AAPL.tail()  # final five rows
AAPL['Adj Close'].head()  # first five rows of single column
AAPL.loc['2016-04-05']  # single row via index value
AAPL.iloc[:2]  # two rows via index numbers
AAPL['Adj Close'].plot(figsize=(10, 6));

# fully vectorized operation for log return calculation
rets = np.log(AAPL['Adj Close'] / AAPL['Adj Close'].shift(1))
rets.hist(figsize=(10, 6), bins=35)

# fully vectorized calculation of 50 days moving average/trend
AAPL['MA50'] = pd.rolling_mean(AAPL['Adj Close'], window=50)
AAPL[['Adj Close', 'MA50']].plot(figsize=(10, 6));