import sys

def main():
    [c_rectangles, c_points] = list(map(int, sys.stdin.readline().strip("\n").split()))
    rectangles = []
    points = []
    for _ in range(c_rectangles):
        [ax, ay, bx, by] = list(map(int, sys.stdin.readline().strip("\n").split()))
        curr_rectangle = [
            [ax, ay], # lower left 
            [ax, by], # upper left
            [bx, by], # upper right
            [bx, ay], # lower right
        ]
        rectangles.append(curr_rectangle)

    points_on_rect = [0] * c_rectangles


    for _ in range(c_points):
        [x, y] = list(map(int, sys.stdin.readline().strip("\n").split()))
        points.append([x, y])

    for rectangle in range(len(rectangles)):
        count = 0
        for point in range(len(points)):
            if in_rectangle(rectangles[rectangle], points[point]):
                count += 1
        points_on_rect[rectangle] = count
    
    a = 0
    for i in rectangle:
        print(i, end=" ")
        a += 1
        if a == 5:
            print("\n")
    print(points_on_rect.index(max(points_on_rect)) + 1)


def in_rectangle(rectangle, point):
    if rectangle[0][0] <= point[0] <= rectangle[2][0] and rectangle[0][1] <= point[1] <= rectangle[1][1]:
        return True
    else:
        return False
    
main()