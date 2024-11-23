def maximumProfit(prices):
    n = len(prices) -1
    lMin = prices[0]
    lMax = prices[0]
    res = 0

    i = 0
    while i < n:
        while 1 < n and prices[i] >= prices[i + 1]:
            i += 1
        lMin = prices[i]
        while i < n and prices[i] <= prices[i + 1]:
            i += 1
        lMax = prices[i]
        res += lMax - lMin
    return res
if __name__ == "__main__":
    prices = [100,180,260,310,40,535,695]
    print(maximumProfit(prices))