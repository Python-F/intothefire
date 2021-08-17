import json
import random

f=open('dialogues.json',)
dialogues=json.load(f)

print(dialogues['0'])
while(True):
    ready = input('yes or no >')
    if ready.lower() == 'yes':
        print(dialogues['1'])
        break
    elif ready.lower() == 'no':
        print(dialogues['2'])
        break
    else:
        continue












def maze_gen(size):
    m = [[0] * size for i in range(size)]
    m[0][0] = 1
    m[-1][-1] = 1

    for i in m:
        r = random.randint(1,4)
        for j in i:
            if r == 1:
                m[i][j] = 1

    return m






