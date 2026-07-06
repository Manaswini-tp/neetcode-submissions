class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1 for _ in nums]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j==i:
                    continue
                res[j]=res[j]*nums[i]
        return res