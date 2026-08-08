class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftmax = height[0]
        rightmax = height[n-1]
        res = 0
        l, r = 0, n-1
        while l<=r:
            if leftmax<rightmax:

                if height[l] > leftmax:

                        leftmax = height[l]

                else:

                    res += leftmax - height[l]
                l=l+1

            else:
                if height[r] > rightmax:

                        rightmax = height[r]

                else:

                    res += rightmax - height[r]
                r = r-1
        return res