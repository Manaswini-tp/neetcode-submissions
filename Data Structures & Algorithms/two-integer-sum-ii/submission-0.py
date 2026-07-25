class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1
        a = [0]*2
        while l<r:
            if numbers[l]+numbers[r]==target:
                a[0] = l+1
                a[1] = r+1
                break
            elif numbers[l]+numbers[r]>target:
                r=r-1
            else:
                l=l+1
        return a