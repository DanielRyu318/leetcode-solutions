class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        shorter, longer = (nums1, nums2) if len(nums1)<=len(nums2) else (nums2, nums1)

        counts = {}
        for i in shorter:
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 1

        ans = []
        for j in longer:
            if j in counts and counts[j] > 0:
                counts[j] -= 1
                ans.append(j)

        return ans
