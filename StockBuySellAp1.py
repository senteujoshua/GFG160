def maxProfitRec(price, start, end):
    res = 0

    for i in range(start, end):
        for j in range(i+1, end):
            if price[j] > price[i]:
                curr = (price[j] - price[i]) + \
                maxProfitRec(price, start, i-1) +\
                maxProfitRec(price, j+1, end)
                res = max(res,curr)

    return res


def maximumProfit(prices):
    return maxProfitRec(prices, 0, len(prices) - 1)




if __name__ == "__main__":
    prices = [100,180,260,310,40,535,695]
    print(maximumProfit(prices))