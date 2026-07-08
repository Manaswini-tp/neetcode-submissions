class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        count = 1
        longest = 1
        if len(nums)==0:
                count=0
                longest=0
        for i in range(len(nums)-1):
            
            if nums[i+1]-nums[i]==1:
                count+=1
            elif nums[i+1]-nums[i]==0:
                continue
            else:
                count=1
            longest = max(longest,count)
        return longest