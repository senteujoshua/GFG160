def max_product(arr):
    n = len(arr)
    currMax = arr[0]
    currMin = arr[0]
    maxProd = arr[0]
    for i in range(1, n):
        temp = max(arr[i],currMax * arr[i],currMin * arr[i])
        currMin = min(arr[i],currMax * arr[i],currMin * arr[i])
        currMax = temp
        maxProd = max(maxProd, currMax)
    return maxProd

if __name__  == "__main__":
    arr = [-2,6,-3,-10,0,2]
    print(max_product(arr))  # Output: 6