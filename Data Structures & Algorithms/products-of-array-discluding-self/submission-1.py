class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        post = [1 for _ in nums]
        for i in range(len(nums)-1,-1,-1):
            if i==len(nums)-1:
                post[i] = 1
                continue
            post[i] = post[i+1]*nums[i+1]
        pre = [1 for _ in nums]
        for i in range(0,len(nums)):
            if i==0:
                pre[i] = 1
                continue
            pre[i] = pre[i-1]*nums[i-1]
        res = [1 for _ in nums]
        for i in range(len(nums)):
            res[i] = pre[i]*post[i]
        return res