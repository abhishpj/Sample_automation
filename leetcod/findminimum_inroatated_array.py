""""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.


"""


class Solution(object):

    def findMin1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return min(nums)

    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter =0j
        l_length=len(nums)
        while l_length>0:
            mid=l_length-1/2




if __name__ == "__main__":
    x=Solution()
    y=[3,4,5,1,2]
    print x.findMin(y)