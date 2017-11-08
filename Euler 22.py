# Project Euler number 22

with open('names.txt','r') as n:
    names = n.read()

names = names.replace('"', '')
names  = names.split(',')
names.sort() 

scoreTotal = 0

for i, name in enumerate(names):
    score = 0
    for letter in name:
        score = score + (ord(letter)-64)
    score = score * (i+1)
    scoreTotal = scoreTotal + score

print(scoreTotal)

