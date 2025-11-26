class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        m = len(flowerbed)
        i = 0
        
        while i < m and n > 0:
            if flowerbed[i] == 0:
                if i == 0:
                    prev=0
                else:
                    prev=flowerbed[i-1]
                if i == m-1:
                    next=0
                else:
                    next=flowerbed[i+1]
                
                if prev == 0 and next == 0:
                    flowerbed[i] = 1
                    n -= 1
                    i += 2
                    continue
            i += 1
        
        return n == 0
def test_helper(flowerbed, n, expected):
    sol = Solution()
    res = sol.canPlaceFlowers(flowerbed[:], n)  # use copy so original not modified
    print(flowerbed, n, expected, res)
    assert res == expected


def test():
    test_helper([1,0,0,0,1], 1, True)
    test_helper([1,0,0,0,1], 2, False)
    test_helper([0], 1, True)
    test_helper([0,0,0], 2, True)
    test_helper([1,0,1,0,1,0,1], 1, False)
    test_helper([0,0,1,0,0], 2, True)

if __name__ == "__main__":
    test()