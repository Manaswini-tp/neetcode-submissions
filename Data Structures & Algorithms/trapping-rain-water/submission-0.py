class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        res = 0
        for i in range(len(height)):
            if i==0:
                continue
            leftmax, rightmax = 0,0
            for k in range(0, i+1):
                leftmax = max(leftmax, height[k])
            
            for j in range(i+1, len(height)):
                rightmax = max(rightmax, height[j])
            mini = min(leftmax, rightmax)
            if mini-height[i]<0:
                continue
            res = res + (mini-height[i])
        return res
            
