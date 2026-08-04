class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        i = 0
        for i in range(len(nums)-2):
            j, k = i+1, len(nums)-1
            while(j<k):
                if nums[i]+nums[j]+nums[k]==0:
                    tmp = [nums[i],nums[j],nums[k]]
                    res.add(tuple(tmp))
                    j=j+1
                    k=k-1
                elif nums[i]+nums[j]+nums[k]>0:
                    k = k-1
                else:
                    j=j+1 
        return [list(i) for i in res]