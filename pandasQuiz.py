# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 09:25:23 2024

@author: Surya Hardiansyah
"""
import pandas as pd

data = {'col1':[10,20,30],
'col2':[111,222,333],
'col3':['a','b','c']}

df = pd.DataFrame(data)
df

a = df.loc[[0,2], ['col1','col3']]
b = df.iloc[[0,2], [0,2]]
c = df[['col1', 'col3']].iloc[[0,2]]

a == b
a == c
b == c