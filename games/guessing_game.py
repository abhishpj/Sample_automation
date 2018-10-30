""""
In this game we will add a counter for how many guesses the user can have.

The counter is initial set to zero.

The while loop will run as long as the guesses are less to 5.

If the user guess the right number before that, the script will break and
present the user with how many guesses it took to guess the right number.

The variables in this script can be changed to anything.
"""
from __future__ import print_function
import random


class Guess(object):
    lower = 0
    upper = 30

    def __init__(self):
        self.running = 0
        self.input = None
        self.randm = None

    def start_guess(self):
        while self.running < 5:
            self.input = int(raw_input("enter the number\n"))
            self.randm = self.generate_random()
            if self.randm == self.input:
                print("Numbers matched ", self.input)
            elif self.randm != self.input:
                print("numbers didnt match random number is ", self.randm)
            else:
                pass
            self.running += 1

    @classmethod
    def generate_random(cls):
        return random.randint(cls.lower,cls.upper)

if __name__ == "__main__":
    x=Guess()
    x.start_guess()