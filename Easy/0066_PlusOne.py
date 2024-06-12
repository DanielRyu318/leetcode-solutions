class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        digits[-1] += 1
        digits = digits[::-1]
        
        for i,num in enumerate(digits):
            if num == 10:
                digits[i] = 0
                if i == len(digits)-1:
                    digits.append(1)
                    break
                digits[i+1] += 1

        return digits[::-1]
