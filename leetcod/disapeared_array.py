""""Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
"""


class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = []
        s_num = set(nums)
        print s_num
        y = 1 + len(nums)
        for i in xrange(1, y):
            if i not in s_num:
                l.append(i)
        return l


if __name__ == "__main__":
    x=Solution()
    y=[1,23,25,25,24,27,28,30]
    print x.findDisappearedNumbers(y)