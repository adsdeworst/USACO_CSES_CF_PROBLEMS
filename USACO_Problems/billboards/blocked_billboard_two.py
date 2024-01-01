import sys

def main():
    to_cover = list(map(int, sys.stdin.readline().strip("\n").split()))
    covered = list(map(int, sys.stdin.readline().strip("\n").split()))

    # if only one point is in covered
    [ax, ay, bx, by] = to_cover
    to_cover = [
        [ax, ay], # lower left 
        [ax, by], # upper left
        [bx, by], # upper right
        [bx, ay], # lower right
    ]

    [cx, cy, dx, dy] = covered
    covered = [
        [cx, cy], # lower left 
        [cx, dy], # upper left
        [dx, dy], # upper right
        [dx, cy], # lower right
    ]

    num_points = 0
    points_list = []
    for i in to_cover:
        num_points += points(covered, i)
        if points(covered, i) > 0:
            points_list.append(i)

    if num_points == 1 or num_points == 0:
        print(int((to_cover[1][1] - to_cover[0][1]) * (to_cover[2][0] - to_cover[0][0])))
        return (to_cover[1][1] - to_cover[0][1]) * (to_cover[2][0] - to_cover[0][0])
    elif num_points == 2:
        y_bound_covered = [covered[0][1], covered[1][1]] # cy, dy
        x_bound_covered = [covered[0][0], covered[2][0]] # cx, dx
        y_bound_to_cover = [to_cover[0][1], to_cover[1][1]]
        x_bound_to_cover = [to_cover[0][0], to_cover[2][0]]    
        if x_bound_covered[0] < x_bound_to_cover[0] and x_bound_to_cover[1] < x_bound_covered[1]:
            interescting_area = (y_bound_covered[0] - y_bound_to_cover[0]) * (x_bound_to_cover[1] - x_bound_to_cover[0])
        elif y_bound_covered[0] < y_bound_to_cover[0] and y_bound_to_cover[1] < y_bound_covered[1]:
            interescting_area = (x_bound_to_cover[1] - x_bound_covered[1]) * (y_bound_to_cover[1] - y_bound_to_cover[0])
        print(interescting_area)
        return interescting_area
    else:
        print(0)
        return 0

def points(rectangle, coord):
    y_bound = [rectangle[0][1], rectangle[1][1]]
    x_bound = [rectangle[0][0], rectangle[2][0]]
    if y_bound[0] < coord[1] < y_bound[1] and x_bound[0] < coord[0] < x_bound[1]:
        return 1
    else:
        return 0

main()