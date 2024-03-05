import sys

def main():
    N = int(input())
    locations = []
    for _ in range(N):
        locations.append(list(map(int, input())))
    locations.sort()
    
    