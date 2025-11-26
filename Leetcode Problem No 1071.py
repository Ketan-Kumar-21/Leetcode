class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""

        from math import gcd
        g = gcd(len(str1), len(str2))
        return str2[:g]
        

 
def test_helper(s1,s2,expected):
    sol=Solution()
    res=sol.gcdOfStrings(s1,s2)
    print(s1,s2,expected,res)
    assert res == expected
def test():
    test_helper("ABABAB","ABAB","AB")
    test_helper("ADHGH","ABCD","")
    test_helper("AAAAA","A","A")
    test_helper("CCCCC","CC","C")
if __name__ == "__main__":
    test()