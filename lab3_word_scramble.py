# course: Object-oriented programming, year 2, semester 1
# academic year: 201920
# author: B. Schoen-Phelan
# date: 08-10-2019
# purpose: Lab 3

import string
import random

class WordScramble:
    def __init__(self):
        self.user_input = input("Please give me a sentence: ")

    def scramble(self):
        # print what was input

        print("The user input was: ", self.user_input)
        user = list(self.user_input.split())
        #
        # # first scramble is just one word
        #
        random.shuffle(user)
        print(user)
        #
        # # reverse two indices
        #
        temp = user[0]
        user[0] = user[-1]
        user[-1] = temp
        print(user)

        # particularly good to use is to switch the first two
        # and the last two
        # this only makes sense if you have a world that is longer than 3


        # now try to scramble one sentence
        # do just words first, then you can move on to work on
        # punctuation
        new = list(self.user_input.split())

        for i, word in enumerate(new):
            if len(word) > 3:
                ran = list(word)
                random.shuffle(ran)
                print(ran)

                s = ""
                for x in ran:
                    s += x

            new[i] = s

        print(new)

word_scrambler = WordScramble()
word_scrambler.scramble()

