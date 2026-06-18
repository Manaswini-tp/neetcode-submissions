class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        m = len(nums)
        n = len(set(nums))
        if m==n:
            return False
        return True