class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        # Initialize pointers for nums1, nums2, and the merge position
        index1 = m - 1
        index2 = n - 1
        index_merge = m + n - 1

        # Traverse from the end of nums1 and nums2
        while index2 >= 0:
            # Compare elements and place the larger one in the correct position
            if index1 >= 0 and nums1[index1] > nums2[index2]:
                nums1[index_merge] = nums1[index1]
                index1 -= 1
            else:
                nums1[index_merge] = nums2[index2]
                index2 -= 1
            index_merge -= 1
