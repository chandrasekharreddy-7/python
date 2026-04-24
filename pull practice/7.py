def max_profit(prices: list) -> int:
    min_price = prices[0]
    max_profit_value = 0
    for price in prices:
        if price < min_price:
            min_price = price
        profit = price - min_price
        if profit > max_profit_value:
            max_profit_value = profit
    return max_profit_value
print(max_profit([7, 1, 5, 3, 6, 4]))  # 5
print(max_profit([7, 6, 4, 3, 1]))     # 0
print(max_profit([1, 2, 3, 4, 5]))     # 4
print(max_profit([3, 8, 1, 9]))        # 8