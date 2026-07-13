import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt


wtd=yf.download('CL=F',start='2020-01-01', end='2024-12-31')
brent=yf.download('BZ=F',start='2020-01-01', end='2024-12-31')



