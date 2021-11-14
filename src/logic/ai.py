import random

class AI:

    def __init__(self, beat):
        self.beat = {'R':'P', 'P':'S', 'S':'R'}

    def play(self):
        return list(self.beat.keys())[random.randint(0,2)]