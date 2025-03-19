'''
#BRUTE FORCE APP[TC=O(nlogn)]

class Solution:
    def largest(self, arr):
        # code here
        n=len(arr)
        arr=sorted(arr)
        return arr[n-1]
'''

#OPTIMAL APP[TC=o(n)]

class Solution:
    def largest(self, arr):
        n=len(arr)
        max=arr[0]
        for num in arr:
            if num > max:
                max=num
        return max
