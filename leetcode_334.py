class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        first = float('inf')
        second = float('inf')

        for x in nums:
            if x <= first:
                first = x
            elif x <= second:
                second = x
            else:
                return True

        return False


def test_helper(nums, expected):
    sol = Solution()
    result = sol.increasingTriplet(nums)
    print(nums, expected, result)
    assert result == expected


def test():
    test_helper([1,2,3,4,5], True)
    test_helper([5,4,3,2,1], False)
    test_helper([2,1,5,0,4,6], True)
    test_helper([20,100,10,12,5,13], True)
    test_helper([1,1,1,1], False)
    test_helper([1,2], False)
    test_helper([2,4,-2,-3], False)
    test_helper([2,1,5,0,3], False)
    test_helper([1,5,0,4,1,3], True)


if __name__ == "__main__":
    test()
