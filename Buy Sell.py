# this writes a problem to find the best buy and sell option

import random
prices = []
for _ in range(10):
    prices.append(random.randint(10,50))

print(prices)
max_profit  = 0
buy_price = prices[0]

for price in prices:
    buy_price = min (buy_price, price)
    max_profit = max (max_profit, price - buy_price)

print(max_profit, buy_price) # this gives buy_price when minimum on the last day. 
