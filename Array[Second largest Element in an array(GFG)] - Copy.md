'''
#BRUTE FORCE APP WITH TC = O(nlogn)+o(n)
class Solution:
    def getSecondLargest(self, arr):
        n=len(arr)
        arr=sorted(arr)
        for i in range(n-1,-1,-1):
            if arr[i] != arr[n-1]:
                return arr[i]
        return -1


#BETTER APP WITH TC =O(2n)

class Solution:
    def getSecondLargest(self, arr):
        n=len(arr)
        largest=arr[0]
        for num in arr:
            if num > largest:
                largest=num
        second_largest=-1
        for num in arr:
            if num > second_largest and num < largest:
                second_largest=num
        return second_largest
'''
#Optimal APP WITH TC =O(n)
class Solution:
    def getSecondLargest(self, arr):
        n=len(arr)
        largest=arr[0]
        second_largest=-1
        for num in arr:
            if num > largest:
                second_largest=largest
                largest=num
            elif second_largest<num < largest:
                second_largest=num
        return second_largest