class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        substring = []
        max_len = 0

        for i in range(len(s)):
            substring.append((s[i]))
            for j in range(i+1,len(s)):
                if s[j] not in substring[i]:
                    substring[i] += s[j]
                else:
                    break
        for s in substring:
            if len(s)>max_len:
                max_len = len(s)
        
        return max_len
