class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        l = m+n
        arr = [0]*l
        for i in range(n):
            arr[i] = nums1[i]
        for j in range(m):
            arr[j+n] = nums2[j]
        arr.sort()
        for i in range(l):
            print(arr[i])
        if l%2==0:
            mid = int(l/2)
            print(mid)
            res = (arr[mid]+arr[mid-1])/2
        else:
            mid = l//2
            res = arr[mid]
        return res