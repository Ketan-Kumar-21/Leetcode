class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for ch in t:
            if i < len(s) and ch == s[i]:
                i += 1
        return i == len(s)


def test_helper(s, t, expected):
    sol = Solution()
    result = sol.isSubsequence(s, t)
    print(s, t, expected, result)
    assert result == expected


def test():
    test_helper("abc", "ahbgdc", True)
    test_helper("axc", "ahbgdc", False)
    test_helper("", "abc", True)
    test_helper("abc", "", False)
    test_helper("abc", "abc", True)
    test_helper("aaa", "aa", False)
    test_helper("ace", "abcde", True)
    test_helper("a", "a", True)
    test_helper("a", "b", False)


if __name__ == "__main__":
    test()
