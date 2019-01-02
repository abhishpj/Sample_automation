"""
829. Consecutive Numbers Sum
Hard

Given a positive integer N, how many ways can we write it as a sum of consecutive positive integers?

Example 1:

Input: 5
Output: 2
Explanation: 5 = 5 = 2 + 3
"""

class Solution(object):
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        k=N/2

        for i in range(0,N):



if __name__ == "__main__":
    x=Solution()
    y=9
    print x.consecutiveNumbersSum(y)