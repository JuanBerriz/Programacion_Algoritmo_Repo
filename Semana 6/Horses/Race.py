import random

class Race:
    def __init__(self, number, horse_list):
        self.number = number
        self.horse_list = horse_list

    def start_race(self):
        print("And we're off!!!!")

    def winning_horse(self):
        print("The winner is: ", random.choice(self.horse_list))

    