import sys

def main():
    n = int(sys.stdin.readline().strip("\n"))
    expected = []
    gotten = []
    for _ in range(n):
        expected.append(sys.stdin.readline().strip("\n").split())
    
    for _ in range(n):
        gotten.append(sys.stdin.readline().strip("\n").split())

    count = 0
    for i in range(n):
        for k in range(len(expected[i])):
            curr_string = ""
            for j in range(len(expected[i][k])-1, -1, -1):
                curr_string += expected[i][k][j]
            
            if curr_string != gotten[i][k]:
                count += 1

    print(count)

main()