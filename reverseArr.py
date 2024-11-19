def reverseArrayRec(arr,l,r):
    if l >= r:
        return
    
    arr[l], arr[r] = arr[r], arr[l]

    reverseArrayRec(arr, l+1, r-1)


def reverseArray(arr):
    n = len(arr)
    reverseArrayRec(arr, 0, n-1)

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6]
    reverseArray(arr)
    print(arr)  # Output: [6, 5, 4, 3,