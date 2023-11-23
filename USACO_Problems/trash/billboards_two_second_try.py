def in_bounds(bounds, value):
    bounds = sorted(bounds)
    if bounds[0] < value < bounds[1]:
        return True
    else:
        return False
    
def get_value_in_bound(bounds, value):
    bounds = sorted(bounds)
    if in_bounds(bounds, value):
        return bounds[1] - value
    else:
        return bounds[1] - bounds[0]
    
def get_area(bottom_coord, top_coord):
    return abs(bottom_coord[0] - top_coord[0]) * abs(bottom_coord[1] - top_coord[1])

def main():
    with open('billboard.in', 'r') as f:
        [x1, y1, x2, y2] = list(map(int, f.readline().strip("\n").split()))
        [X1, Y1, X2, Y2] = list(map(int, f.readline().strip("\n").split()))
        lawnmower_billboard = [(x1, y1), (x2, y2)]
        cow_feed_billboard = [(X1, Y1), (X2, Y2)]
    
    x_bounds = [lawnmower_billboard[0][0], lawnmower_billboard[1][0]]
    y_bounds = [lawnmower_billboard[0][1], lawnmower_billboard[1][1]]
    ans = get_area(lawnmower_billboard[0], lawnmower_billboard[1])

    for i in lawnmower_billboard:
        if in_bounds(x_bounds, i[0]) != in_bounds(y_bounds, i[1]):
            ans = get_value_in_bound(x_bounds, i[0]) * get_value_in_bound(y_bounds, i[1])

    if min(X1, X2) <= x1 <= max(X1, X2) and min(X1, X2) <= x2 <= max(X1, X2) and min(Y1, Y2) <= y1 <= max(Y1, Y2) and min(Y1, Y2) <= y2 <= max(Y1, Y2):
        ans= 0

    with open('billboard.out', 'w') as f:
        f.write(str(ans))

if __name__ == "__main__":
    main()