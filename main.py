import json

f=open('dialogues.json',)
dialogues=json.load(f)
print(dialogues['0'])
print(dialogues['1'])

