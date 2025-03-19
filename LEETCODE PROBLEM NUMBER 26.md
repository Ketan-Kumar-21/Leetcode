LEETCODE PROBLEM 26 : https://leetcode.com/problems/remove-duplicates-from-sorted-array

#BRUTE FORCE APP WITH TC=O(n)+O(nlogn)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        st=set()
        for num in nums:
            st.add(num)
            nums[:len(st)]=sorted(st)
        return len(st)
'''
#Better App WITH Tc=O(n)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        i=0
        for j in range(1,n):
            if nums[j] != nums[i]:
                nums[i+1]=nums[j]
                i += 1
        return i+1    