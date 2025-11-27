#Brute Force App:
#TC: O(2n) & SC: O(n)
'''
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        
        #Do not return anything, modify nums in-place instead.
    
        arr = []
        for num in nums:
            if num != 0:
                arr.append(num)
        
        k = len(nums) - len(arr)
        for i in range(k):
            arr.append(0)
        
        for i in range(len(nums)):
            nums[i] = arr[i]
'''


#Optimal App:
#TC: O(n) & SC: O(1)
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        i = 0
        n = len(nums)
        for j in range(n):
            if nums[j] != 0:
                if i != j:
                    nums[i], nums[j] = nums[j], nums[i]
                i += 1


def test_helper(nums, expected):
    sol = Solution()
    arr = nums.copy()
    sol.moveZeroes(arr)
    print(nums, expected, arr)
    assert arr == expected


def test():
    test_helper([0,1,0,3,12], [1,3,12,0,0])
    test_helper([0], [0])
    test_helper([1,2,3], [1,2,3])
    test_helper([0,0,1], [1,0,0])
    test_helper([4,2,4,0,0,3,0,5,1,0], [4,2,4,3,5,1,0,0,0,0])
    test_helper([1], [1])
    test_helper([2,0], [2,0])


if __name__ == "__main__":
    test()

