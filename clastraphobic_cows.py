import sys
import math

def main():
    points = []
    for _ in range(int(sys.stdin.readline().strip("\n"))):
        points.append(list(map(int, sys.stdin.readline().strip("\n").split())))
        
    dist = 100000000
    number = [0, 0]   
    
    for i in range(len(points)):
        for k in range(len(points)):
            if points[i] != points[k]:
                curr_dist = get_distance(points[i], points[k])
                if curr_dist < dist:
                    dist = curr_dist
                    number = [i + 1, k + 1]

    print(str(number[0]) + " " + str(number[1]))

    
def get_distance(a, b):
    return math.sqrt(math.pow(a[0]-b[0], 2)+math.pow(a[1]-b[1], 2))

main()