"""
The stock span problem is a financial problem where we have a series of n daily price quotes for a stock and we need to calculate span of stock’s price for all n days. 
The span Si of the stock’s price on a given day i is defined as the maximum number of consecutive days just before the given day, for which the price of the stock on the current day is less than its price on the given day. 
For example:
Input:                              Output:
100, 80, 60, 70, 60, 75, 85         1, 1, 1, 2, 1, 4, 6
"""

prices = list(map(int, input().split(",")))
span_values = []
for i in range(len(prices)):
    counter = 1
    for j in range(i,0,-1):
        if prices[i] > prices[j-1]:
            counter += 1
        else:
            break
    span_values.append(counter)
print(span_values)