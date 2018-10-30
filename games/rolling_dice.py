from __future__ import print_function
import random


class Dice(object):

    lower_boud = 1
    upper_bound = 6

    def __init__(self):
        self.input = ''
        self.roll_again = True

    def start_dice(self):
        while self.roll_again:
            print("Rolling the dice ")
            print(self.generate_random())
            print(self.generate_random())
            self.input =raw_input("Enter T to continue rolling ")
            if self.input != 'T':self.roll_again = False

    @classmethod
    def generate_random(cls):
        return random.randint(cls.lower_boud,cls.upper_bound)

if __name__ == "__main__":
    x=Dice()
    x.start_dice()