class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [1] * n

        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res


def test_helper(nums, expected):
    sol = Solution()
    res = sol.productExceptSelf(nums)
    print(nums, expected, res)
    assert res == expected


def test():
    test_helper([1,2,3,4], [24,12,8,6])
    test_helper([0,1,2,3], [6,0,0,0])
    test_helper([0,0,5,7], [0,0,0,0])
    test_helper([5,1,1,1], [1,5,5,5])
    test_helper([2,3], [3,2])
    test_helper([10], [1])  


if __name__ == "__main__":
    test()
