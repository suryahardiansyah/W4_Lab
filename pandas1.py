import pandas
import pandas as pd
from pandas import DataFrame

pandas.DataFrame
pd.DataFrame
DataFrame

data = {'month'   :[1, 2, 3], 
        'unemp_il':[5.6, 5.7, 5.8], 
        'unemp_wi':[6.1, 6.0, 6.1], 
        'gdp_il'  :[6, 6, 7], 
        'gdp_wi'  :[4, 5, 4]}

data

df = pd.DataFrame(data)
df

#slide 9
df['month']
df[['unemp_il', 'gdp_il']]

cols = ['unemp_wi', 'gdp_wi']
df[cols]

df[[c for c in df.columns if c.endswith('wi')]]

#slide 14
import numpy as np
np.mean(df['unemp_il'])
df['unemp_il'].mean()

#slide 16
df[1:]

df.index = ['a', 'b', 'c']
df

#slide 18
df.loc['a']
df.loc[['a', 'c']]

df.iloc[0]
df.iloc[[0, 2]]

#slide 20
df.loc[['a', 'c'], ['unemp_il', 'gdp_il']]
df.iloc[[0, 2], [1, 3]]

#slide 22
df1 = df[['unemp_il', 'unemp_wi']]
df1

df2 = df.loc[:, ['unemp_il', 'unemp_wi']]
df2

df1['il_rescaled'] = df1['unemp_il'] * .01
df2['il_rescaled'] = df2['unemp_il'] * .01
