# WTI vs Brent Crude Spread Analysis

## Overview
Analysis of the price spread between WTI and Brent crude oil benchmarks (2020-2024). 
This project identifies periods of unusual spread widening and narrowing with annotations 
for key market events including OPEC production cuts and geopolitical events.


## Background: WTI vs Brent Explained

WTI (West Texas Intermediate) and Brent are the two major global oil benchmarks.

**WTI** — American oil, drilled in Texas. Lighter and easier to refine. 
Priced in USD per barrel. The benchmark for US oil markets. 
Stored and delivered at Cushing, Oklahoma.

**Brent** — North Sea oil (UK/Norway). Slightly heavier. Used as the 
global benchmark — when you see "oil price" on the news they're usually 
talking about Brent.

**Why are they different prices?**
Different quality, different location, different shipping costs. 
Brent is usually a few dollars more expensive than WTI.

**The spread:**
Spread = Brent price - WTI price

Normally around $2-5. But sometimes it widens dramatically:
- 2011 — spread hit $27 due to a US supply glut at Cushing
- 2020 — WTI went negative (-$37) while Brent stayed positive because US storage was full
- 2022 — Brent spiked more than WTI due to Europe's dependence on Russian oil

**Why traders care:**
If you're buying and selling oil, an unusually wide or narrow spread signals 
where market stress is occurring. It's one of the first things a commodity 
trader checks every morning.




## Tools
- Python
- pandas
- NumPy
- matplotlib
- yfinance

## What this project covers
- Downloading and cleaning historical oil price data
- Calculating the daily WTI/Brent spread
- Computing rolling volatility
- Visualising spread trends with annotated key events

## Key concepts
The WTI/Brent spread is one of the most closely monitored metrics in commodity trading. 
WTI (West Texas Intermediate) and Brent crude are the two global oil benchmarks — 
understanding their relationship reveals insights about supply/demand dynamics, 
transportation costs and geopolitical risk.

## Status
Complete

## Key Findings
- WTI and Brent prices move almost identically, confirming their role as correlated global benchmarks
- The spread normally sits between $2-6, reflecting transportation and quality differences
- April 2020 (COVID crash): spread spiked to $60+ as WTI went negative (-$37) due to US storage hitting capacity while Brent remained positive — the most extreme spread event in modern oil history
- Mid-2022 (Ukraine war/energy crisis): both benchmarks peaked above $120 with Brent rising faster than WTI due to Europe's heavier dependence on Russian oil
- Volatility has significantly calmed since 2023 with the spread returning to its historical $2-4 range
- Rolling volatility analysis clearly identifies the two major market stress periods (2020 and 2022) without needing any external data
