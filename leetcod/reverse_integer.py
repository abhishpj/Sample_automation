"""Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
"""

class Reverse():

    def __init__(self):
        self.str = None
        self.result = int()

    def reverse(self,num):
        self.str =num
        print self.str
        l=0
        if abs(self.str) > 2147483647:
            return 0
        else:
            while self.str != 0:
                if self.str >= 0:
                    self.str = self.str
                else:
                    self.str=-self.str
                self.result = self.result*10 +self.str%10
                self.str=self.str/10
            if abs(self.result) > 2147483647:
                return 0
            else:
                if num >=0:
                    return self.result
                else:
                    return -self.result

if __name__ == "__main__":
    obj=Reverse()
    print obj.reverse(1534236469)