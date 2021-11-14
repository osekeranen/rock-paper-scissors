import random

beat = {'R':'P', 'P':'S', 'S':'R'}

output = list(beat.keys())[random.randint(0,2)]
print('A.I. plays:', output)
input = input('Human plays: ')

if input == beat[output]:
    print('Human wins!')
elif output == beat[input]:
    print('A.I. wins!')
else:
    print('Draw.')