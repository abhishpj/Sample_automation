"""Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
"""
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        l_len = len(digits)
        num = digits[l_len-1]+1
        if num <9:
            digits[l_len-1]=num
        else:
            for i,v in enumerate(str(num)):
                if i==0:
                    digits[l_len - 1] = int(v.strip())
                elif i==1:
                    digits.append(int(v.strip()))
        return digits
if __name__ == "__main__":
    obj=Solution()
    x=[1,2,3]
    print obj.plusOne(x)