import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt


wti=yf.download('CL=F',start='2020-01-01', end='2024-12-31')
brent=yf.download('BZ=F',start='2020-01-01', end='2024-12-31')


'''Flatten the MultiIndex columns on both datasets'''
wti=wti.droplevel(1,axis=1)
brent=brent.droplevel(1,axis=1)



#1-explore the data

print("\n checking wti and brent data")

print("\n number of the columns and rows")
print(wti.shape)
print(brent.shape)

print("\n the columns information")
print(wti.columns)
print(brent.columns)


print("\n the stats about both of the datasets")
print(wti.describe())
print(brent.describe())


print("\n the first 5 lines of information of each")
print(wti.head())
print(brent.head())


#2-cleaning the data 

'''in this project we'd only need the close column for each data '''

wti=wti[['Close']]
brent=brent[['Close']]



'''Joins both DataFrames side by side — so instead of two separate tables you get one table with both Close prices on the same rows (dates).
Removes any dates where one of them is missing — that's how we align the 1257 vs 1258 row difference.
'''
df=pd.contact([wti,brent],axis=1)
df.columns=['WTI','Brent']
df=df.dropna()


