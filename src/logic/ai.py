import random

class AI:

    beat = {'R':'P', 'P':'S', 'S':'R'}

    """
    def __init__(self):
        pass
    """

    def play():
        return list(AI.beat.keys())[random.randint(0,2)]