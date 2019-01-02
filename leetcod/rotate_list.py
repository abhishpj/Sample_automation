""""Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
"""
from collections import deque

class Solution(object):

    def __init__(self):
        self.dq=deque()
        self.result=[]
    #non inplace rotation
    def rotate1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.

        """
        self.dq = deque(nums)
        print id(nums)
        self.dq.rotate(k)
        nums = list(self.dq)
        print id(nums)
    #inplace rotation without depth
    def rotate2(self,nums,k):
        lstemp = nums[-1]
        llength = len(nums)
        for i, element in enumerate(nums):
            nums[llength-i-1]=nums[llength-i-2]
        nums[0]=lstemp
        print nums

    #inplace rotation with depth
    def rotate(self,nums,k):
        lstemp = nums[-1]
        llength = len(nums)
        counter=0
        while k>counter:
            nums.insert(0, nums.pop())
            print nums
            counter+=1

if __name__ == "__main__":
    x=Solution()
    l=[1,2,3,4,5,6,7]
    print l
    print x.rotate(l,k=2)

