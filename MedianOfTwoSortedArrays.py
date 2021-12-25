class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        if len(nums1) == 0:
            if len(nums2) % 2 == 0:
                return (nums2[len(nums2)//2] + nums2[len(nums2)//2 - 1]) / 2
            else:
                return nums2[len(nums2)//2]
        mid_length = (len(nums1) + len(nums2) + 1) // 2 - 2
        start = -1
        end = len(nums1) - 1
        while True:
            l1 = (start + end) // 2
            l2 = mid_length - l1
            if l1 == -1:
                min_l1 = float('-inf')
            else:
                min_l1 = nums1[l1]
            if l2 == -1:
                min_l2 = float('-inf')
            else:
                min_l2 = nums2[l2]
            if l1 == len(nums1) - 1:
                max_l1 = float('inf')
            else:
                max_l1 = nums1[l1+1]
            if l2 == len(nums2) - 1:
                max_l2 = float('inf')
            else:
                max_l2 = nums2[l2+1]
            if min_l1 <= max_l2 and min_l2 <= max_l1:
                if (len(nums1) + len(nums2)) % 2 == 0:
                    return (max(min_l1, min_l2) + min(max_l1, max_l2)) / 2
                else:
                    return max(min_l1, min_l2)
            elif min_l1 > max_l2:
                end = l1 - 1
            else:
                start = l1 + 1