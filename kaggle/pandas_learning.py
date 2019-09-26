import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

pd.DataFrame({'column A': [1, 2], 'column B': [3, 4]}, index=['Row 1', 'Row 2'])

pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')

# Sample Data
transactions = pd.DataFrame({'date': ['03.01.2013', '03.01.2014', '02.01.2013'], 'item_price': [5, 10, 50],
                             'item_cnt_day': [1.0, 1.0, -1.0]},
                            index=['Row 1', 'Row 2', 'Row 3'])
print(transactions.head())

# String -> Datetime
# transactions.date = pd.to_datetime(transactions.date, format='%d.%m.%Y')

# Other Solution
transactions_new = transactions[transactions['date'].str.endswith('01.2013')]
print(transactions_new)
print(transactions_new['item_price']*transactions_new['item_cnt_day'])
print((transactions_new['item_price'] * transactions_new['item_cnt_day']).groupby(transactions_new['date']).sum().max())
