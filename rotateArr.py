def rotateArr(arr, d):
    n = len(arr)
    d = d % n
    for i in range(d):
        first = arr[0]
        for j in range(n - 1):
            arr[j] = arr[j+1]
        arr[n - 1] = first

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    d = 2
    rotateArr(arr, d)
    print(arr)


