"""Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:

Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
"""


class Solution(object):
    def findMaxConsecutiveOnes(self,nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p_count=0
        t_count=0
        for element in nums:
            if element == 1:
                t_count+=1
                if p_count<t_count:
                    p_count=t_count
            else:
                    t_count=0
        return p_count
if __name__ == "__main__":
    x=Solution()
    y=[]
    print x.findMaxConsecutiveOnes(y),"answer"