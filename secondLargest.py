class Solution:
    def getSecondLargest(self, arr):
        n = len(arr)
        largestNum = -1
        secondLargest = -1
        
        for i in range(n):
            if arr[i]> largestNum:
                secondLargest = largestNum
                largestNum = arr[i]
            if arr[i] < largestNum and arr[i] > secondLargest:
                secondLargest = arr[i]
                
                
                
                
        return secondLargest
