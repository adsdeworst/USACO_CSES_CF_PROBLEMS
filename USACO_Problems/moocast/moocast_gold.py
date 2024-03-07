import sys

class Cow:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        
n = int(input())
cows = []
for _ in range(n):
    (x, y) = list(map(int, input().split()))
    cows.append(Cow(x, y))
    
