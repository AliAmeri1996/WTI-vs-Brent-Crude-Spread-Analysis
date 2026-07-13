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
df=pd.concat([wti,brent],axis=1)
df.columns=['WTI','Brent']
df=df.dropna()




#3-Analysis
df["Spread"]=df['Brent']-df['WTI']

df["Spread_MA30"]=df["Spread"].rolling(30).mean()#for each day it takes that day plus the 29 days before it, calculates the stat on those 30 days combined, then moves forward one day and does it again.
df["Spread_Vol"]=df['Spread'].rolling(30).std()

print(df.head(10))



#4-visulaziation 
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 10))

# Chart 1 - WTI and Brent prices
wti['Close'].plot(ax=ax1, label='WTI')
brent['Close'].plot(ax=ax1, label='Brent')
ax1.set_title('WTI vs Brent Prices')
ax1.set_ylabel('Price (USD)')
ax1.legend()

# Chart 2 - Spread and MA30
df['Spread'].plot(ax=ax2, label='Spread')
df['Spread_MA30'].plot(ax=ax2, label='30 Day MA')
ax2.set_title('WTI vs Brent Spread')
ax2.set_ylabel('Spread (USD)')
ax2.legend()

# Chart 3 - Volatility
df['Spread_Vol'].plot(ax=ax3, label='Volatility')
ax3.set_title('Spread Volatility (30-day Rolling Std)')
ax3.set_ylabel('Volatility (USD)')
ax3.set_xlabel('Date')
ax3.legend()



'''COVID annotation'''
ax2.annotate('COVID crash', 
             xy=('2020-04-20', 60),
             xytext=('2020-08-01', 55),
             arrowprops=dict(arrowstyle='->'))



'''Ukraine War annotation on the chart'''
ax2.annotate('Ukraine War', 
             xy=('2022-03-01', 8),# 8 It's the y position where the arrow points to 
             xytext=('2022-06-01', 20), # 20 It's the x position where the arrow points to
             arrowprops=dict(arrowstyle='->'))

plt.tight_layout()
plt.show()