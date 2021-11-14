import logic.ai

beat = {'R':'P', 'P':'S', 'S':'R'}

output = logic.ai.AI.play()
print('A.I. plays:', output)
input = input('Human plays: ')

if input == beat[output]:
    print('Human wins!')
elif output == beat[input]:
    print('A.I. wins!')
else:
    print('Draw.')