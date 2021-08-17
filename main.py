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








