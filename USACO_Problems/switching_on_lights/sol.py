# notfinished

import sys

def main():
    [n, m] = list(map(int, sys.stdin.readline().strip("\n").split()))
    rooms = []

    for _ in range(m):
        [x, y, a, b] = list(map(int, sys.stdin.readline().strip("\n").split()))
        l = [[x, y],[a, b]]
        rooms.append(l)
    
    rooms.sort(key=lambda x: x[0][0])
    print(rooms)

    start = []
    end = []

    for i in rooms:
        start.append(i[0])
        end.append(i[1])

    print(get_rooms(0, [1, 1], start, end))

def get_rooms(count, current_room, start, end):
    if count == len(start) == len(end):
        return count
    elif current_room not in start:
        return count
    else:
        if current_room in start:
            dest = end[start.index(current_room)]

            start.pop(start[start.index(current_room)])
            count += 1
            current_room = dest
            return get_rooms(count, current_room, start, end)
main()