import pandas as pd

#https://fred.stlouisfed.org/series/GDPC1
path = r'c:\users\jeff levy\downloads\GDPC1.csv'

print('Hello world!\nHow are you?\n')
print(r'Hello world!\nHow are you?\n')

import os
base_path = r'c:\users\jeff levy\downloads'
path = os.path.join(base_path, 'GDPC1.csv')
path

df = pd.read_csv(path)
df

df.head()
df.tail()
df.shape

#slide 9
df.dtypes

df['DATE_2'] = pd.to_datetime(df['DATE'])
df.head()
df.dtypes

#slide 11
df = pd.read_csv(path, parse_dates=['DATE'])
df.head()
df.dtypes

#slide 12
names = {'DATE':'date', 'GDPC1':'gdp'}
df = df.rename(names, axis=1)
df.head()

df2 = pd.DataFrame({'one':[1, 2, 3], 'two':[10, 11, 12]})
df2
df2.mean()
df2.mean(axis=1)

df = df.rename(columns=names)

#slide 16
df.head()
df.tail()
df[df['gdp'] > 10000]
df['gdp'] > 10000

df2
df2[[True, False, True]]

import datetime
start_date = datetime.datetime(1999, 1, 1)
df[df['date'] > start_date]

df[(df['date'] > start_date) & (df['gdp'] < 17000)]

#slide 22
data = {'col1':[1, 2, 'x', 4], 
        'col2':[5, 6, 7, 8], 
        'col3':[9, 10, 11, 12]}
idx = ['a', 'b', 'c', 'd']
df = pd.DataFrame(data, index=idx)
df

def some_math(x):
    return x * 2

df['col1'].map(some_math)

#slide 23
df.loc['c', 'col1'] = 3

def zscore(x):
    return (x - x.mean()) / x.std()

df.apply(zscore)

#slide 24
df.applymap(some_math)

#slide 27
df.apply(lambda x: (x - x.mean()) / x.std())