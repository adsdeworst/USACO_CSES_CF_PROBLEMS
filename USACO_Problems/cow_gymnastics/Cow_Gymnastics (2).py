import sys

input = sys.stdin

k = (input.readlines(1)[0].split())
n = int(k[1])
k = int(k[0])

consistents = []

for i in input.readlines():
    consistents.append(i.split())

input = consistents
consistents = []

for i in range((n)):
    consistents.append([])

for cowNum in range(1, n+1):
    for line in input:
        for cow in range(n):
            if cowNum == int(line[cow]):
                for eachCowNum in line[cow+1:n]:
                    consistents[cowNum-1].append(eachCowNum)

numOfConsitsents = 0

#counter = []
secondCounter = 0

for cowRanking in consistents: #2, 3, 3, 2, 3
    for num in range(1, n+1): #1, 2, 3, 4
        if secondCounter == k:
            numOfConsitsents += 1
        secondCounter = 0
        for eachCow in cowRanking: #2 then 3 then 3 then 2 then 3
            if int(eachCow) == num:
                secondCounter += 1

output = sys.stdout
output.write(str(numOfConsitsents))