def main():
    with open('billboard.in', 'r') as f:
        [x1, y1, x2, y2] = list(map(int, f.readline().strip("\n").split()))
        [X1, Y1, X2, Y2] = list(map(int, f.readline().strip("\n").split()))
        lawnmower_billboard = [(x1, y1), (x2, y2)]
        cow_feed_billboard = [(X1, Y1), (X2, Y2)]
    
    X_bounds = [lawnmower_billboard[0][0], lawnmower_billboard[1][0]]
    y_bounds = [lawnmower_billboard[0][1], lawnmower_billboard[1][1]]
    x_length = 0
    y_length = 0
    ans = 0


    if in_rectangle(lawnmower_billboard, cow_feed_billboard[0]) == True and in_rectangle(lawnmower_billboard, cow_feed_billboard[1]) == True:
        ans = get_area(lawnmower_billboard[0], lawnmower_billboard[1])
    
    elif in_rectangle(lawnmower_billboard, cow_feed_billboard[0]) == True and in_rectangle(lawnmower_billboard, cow_feed_billboard[1]) == False:
        if in_bounds(X_bounds, cow_feed_billboard[0][0]) == True:
            x_length = max(X_bounds) - cow_feed_billboard[0][0]
            y_length = max(y_bounds) - min(y_bounds)
            ans = x_length * y_length
        else:
            x_length = max(X_bounds) - min(X_bounds)
            y_length = max(y_bounds) - cow_feed_billboard[0][1]
            ans = x_length * y_length
    elif in_rectangle(lawnmower_billboard, cow_feed_billboard[0]) == False and in_rectangle(lawnmower_billboard, cow_feed_billboard[1]) == True:
        if in_bounds(X_bounds, cow_feed_billboard[1][0]) == True:
            x_length = max(X_bounds) - cow_feed_billboard[1][0]
            y_length = max(y_bounds) - min(y_bounds)
            ans = x_length * y_length
        else:
            x_length = max(X_bounds) - min(X_bounds)
            y_length = max(y_bounds) - cow_feed_billboard[1][1]
            ans = x_length * y_length
    else:
        ans = 0

    with open('billboard.out', 'w') as f:
        f.write(str(ans))
        print(ans)
'''
lawmower_billboard = [(2, 1), (7, 4)]
cow_feed_billboard = [(5, -1), (10, 3)]
'''
def in_bounds(bounds, value):
    bounds = sorted(bounds)
    if bounds[0] < value < bounds[1]:
        return True


def in_rectangle(lawnmower_billboard, cow_feed_billboard_single_value):
    x_bounds = [lawnmower_billboard[0][0], lawnmower_billboard[1][0]]
    y_bounds = [lawnmower_billboard[0][1], lawnmower_billboard[1][1]]
    x_value = cow_feed_billboard_single_value[0]
    y_value = cow_feed_billboard_single_value[1]
    if in_bounds(x_bounds, x_value):
        if in_bounds(y_bounds, y_value):
            return True
        else:
            return False
    return False
    
def get_area(bottom_coord, top_coord):
    return abs(bottom_coord[0] - top_coord[0]) * abs(bottom_coord[1] - top_coord[1])

if __name__ == "__main__":
    main()