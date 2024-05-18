#Surya Hardiansyah

import pandas as pd

data = {'gdp_usa':[15542, 16197, 16785, 17527, 18238, 18745, 19543], 
        'gdp_canada':[1789, 1829, 1847, 1804, 1556, 1528, 1650], 
        'gdp_mexico':[1181, 1201, 1274, 1315, 1172, 1078, 1159], 
        'unemp_usa':[8.9, 8.1, 7.4, 16.2, 5.3, 4.9, 4.4], 
        'unemp_canada':[7.5, 7.4, 7.2, 7.1, 7, 7.2, 6.4], 
        'unemp_mexico':[7.3, 7, 6.9, 6.6, 6.6, 6.8, 6.1]}

years = [2011, 2012, 2013, 2014, 2015, 2016, 2017]

df = pd.DataFrame(data, index=years)
df
#Try to complete all of the following writing only one line of code each

#1. Select only the GDP columns, for the years 2013-2014.
df.iloc[2:4, 0:3] # row idx 2 before 4, col idx 0 before 3
#2. The unemployment rate in the USA in 2014 should be 6.2, not 16.2.
#   Write one line that replaces that value.
df.loc[2014, 'unemp_usa'] = 6.2 # df.replace(16.2, 6.2) might be problematic
#3. Calculate two new columns named 'unemp_mean_na' and 'gdp_sum_na'
#   that are equal to the mean and sum of the respective columns for
#   these three North American (na) countries in the given years
#   (hint: look up the axis key-word argument in the respective
#   Pandas methods).  You will need one line of code for the sum
#   and one for the mean.
df['unemp_mean_na'] = df[['unemp_usa', 'unemp_canada', 'unemp_mexico']].mean(axis = 1)
df['gdp_sum_na'] = df[['gdp_usa', 'gdp_canada', 'gdp_mexico']].sum(axis = 1)
#4. Display only the values for Canada in 2015 and 2016.
df.loc[[2015, 2016], [c for c in df.columns if c.endswith('canada')]]
#5. Create a new variable that is a subset of the main data showing
#   only columns for Mexico from 2014 and later.
mexico_14_17 = df.loc[2014:2017, [c for c in df.columns if c.endswith('mexico')]]
print(mexico_14_17)
#6. Calculate a new column in this subset called 'gdp_delta' which
#   shows the change in GDP for each country from year to year.  
#   Hint: you'll need to look up a new Series method for this. All 
#   the new values will be NaN for the first year.
# 0:3 used to exclude gdp_sum_na
for column in [c for c in df.columns if c.startswith('gdp')][0:3]: 
    df[f'{column}_delta'] = pd.Series(df[column]).diff()
print(df.iloc[:, -3:]) # see the new delta columns
