class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        if not nums1:
            if len(nums2) % 2 == 0:
                return float(nums2[len(nums2) // 2] + nums2[len(nums2) // 2 - 1]) / 2.0
            else:
                return float(nums2[len(nums2) // 2])
        
        half = (len(nums1) + len(nums2) + 1) // 2

        low = 0
        high = len(nums1)
        while low < high:
            mid = (high + low + 1) // 2
            left1 = nums1[mid - 1] if mid > 0 else -float("inf")
            left2 = nums2[half - mid - 1] if half - mid > 0 else -float("inf")
            right1 = nums1[mid] if mid < len(nums1) else float("inf")
            right2 = nums2[half - mid] if half - mid < len(nums2) else float("inf")
            if max(left1, left2) <= min(right1, right2):
                low = mid
            else:
                high = mid - 1
        
        left1 = nums1[high - 1] if high > 0 else -float("inf")
        left2 = nums2[half - high - 1] if half - high > 0 else -float("inf")
        right1 = nums1[high] if high < len(nums1) else float("inf")
        right2 = nums2[half - high] if half - high < len(nums2) else float("inf")
        if (len(nums1) + len(nums2)) % 2 == 0:
            return float(max(left1, left2) + min(right1, right2)) / 2.0
        else:
            return float(max(left1, left2))

