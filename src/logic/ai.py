import random

class AI:

    def __init__(self, beat):
        self.beat = beat

    def play(self):
        return list(self.beat.keys())[random.randint(0,2)]