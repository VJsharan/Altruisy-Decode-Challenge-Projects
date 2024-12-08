def find_max_profit(prices):
    if len(prices) < 2:
        return 0

    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    
    return max_profit

n = int(input("Enter the input values : "))
prices = [int(input()) for _ in range(n)]

profit = find_max_profit(prices)

print(profit)
