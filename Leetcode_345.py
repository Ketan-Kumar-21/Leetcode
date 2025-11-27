class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = "aeiouAEIOU"
        i, j = 0, len(s) - 1

        while i < j:
            if s[i] in vowels and s[j] in vowels:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
            elif s[i] not in vowels:
                i += 1
            elif s[j] not in vowels:
                j -= 1

        return "".join(s)


def test_helper(inp, expected):
    sol = Solution()
    res = sol.reverseVowels(inp)
    print(inp, expected, res)
    assert res == expected


def test():
    test_helper("hello", "holle")
    test_helper("leetcode", "leotcede")
    test_helper("aA", "Aa")
    test_helper("AEIOU", "UOIEA")
    test_helper("xyz", "xyz")
    test_helper("abecidofu", "ubocidefa")
    test_helper("abecidofu", "ubocidefa")

    test_helper(" ", " ")
    test_helper("", "")


if __name__ == "__main__":
    test()
