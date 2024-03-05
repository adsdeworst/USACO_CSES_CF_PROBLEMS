import sys

sys.stdin = open('paintbarn.in', 'r')
sys.stdout = open('paintbarn.out', 'w')

barn_wall = [[0] * 1000] * 1000
valid_wall = [[False] * 1000] * 1000

rows, k = list(map(int, input().split()))
answer = 0
for _ in range(rows):
    x1, y1, x2, y2 = list(map(int, input().split()))
    for col in range(x1, x2 + 1):
        for row in range(y1, y2 + 1):
            barn_wall[row][col] += 1
            if barn_wall[row][col] == k:
                valid_wall[row][col] == True
                answer += 1 
            elif barn_wall[row][col] > k and valid_wall[row][col]:
                valid_wall[row][col] = False
                answer -= 1

print(answer) 