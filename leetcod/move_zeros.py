"""Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]"""


class Solution(object):

    def moveZeroes1(self,nums):
        llength = len(nums)
        counter=0
        temp_list=[]
        while llength>counter:
            if nums:
                x=nums.pop()
                if x!=0:
                    nums.insert(0,x)
                else:
                    temp_list.append(0)
            counter+=1
        nums.extend(temp_list)
        print nums

    def moveZeroes(self, nums):

        # Loop through the array
        # Find the first number that are not 0
        # Switch it with the nums[0]
        # Now nums[0] has the right value
        #
        # Find the second number that are not 0
        # Switch it with the nums[1]
        # Now nums[1] has the right value
        # ...
        current =0


if __name__ == "__main__":
    obj=Solution()
    x=[0]
    print x
    obj.rotate(x)



