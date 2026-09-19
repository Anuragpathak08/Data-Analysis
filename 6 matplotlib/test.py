import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

l=['name','online_order','book_table','rate','votes','location','rest_type','dish_liked','cuisines','approx_cost(for two people)','listed_in(type)','listed_in(city)']

df = pd.read_csv(r"C:\Users\LENOVO\Downloads\zomato.csv")[l]

df['rate'].isnull().sum() #df['rate'].isnull().sum()
df['rate'] = df['rate'].ffill()
df['rate'] = df['rate'].str.replace('/5','')
df['rate'] = df['rate'].replace('NEW','0')
df['rate'] = df['rate'].replace('-','0')
df['rate'].astype('f')

on_of = df.groupby(['online_order', 'book_table'])