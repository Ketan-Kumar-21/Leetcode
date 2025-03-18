class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        st=set()
        for num in nums:
            st.add(num)
            nums[:len(st)]=sorted(st)
        return len(st)