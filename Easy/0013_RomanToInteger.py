class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romanNumDict = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }

        string_list = list(s)
        value_list = []

        for char in string_list:
            value_list.append(romanNumDict[char])
        value_list = value_list[::-1]

        val = value_list[0]
        for i in range(len(value_list)-1):
            if value_list[i+1] >= value_list[i]:
                val += value_list[i+1]
            else:
                val-= value_list[i+1]
        
        return val
