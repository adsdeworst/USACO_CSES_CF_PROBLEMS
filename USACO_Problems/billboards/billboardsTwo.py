def main():
    with open('billboards.in', 'r') as f:
        coord_list = []
        for _ in range(3):
            temp_list = f.readline().strip("\n").split()
            coord_list.append([(int(temp_list[0]), int(temp_list[1])), (int(temp_list[2]), int(temp_list[3]))])
        billboard_a = coord_list[0]
        billboard_b = coord_list[1]
        truck = coord_list[2]
    ans = 0

    a_area = get_area(billboard_a) - get_intersecting_areas(billboard_a, truck)
    b_area = get_area(billboard_b) - get_intersecting_areas(billboard_b, truck)

    with open('billboards.out', 'w') as f:
        f.write(str(a_area + b_area))

def get_intersecting_areas(billboard, truck): #billboard contains two pairs, representing the edges of the billbaord. Same with the truck
    billboard_lower = billboard[0]
    billboard_upper = billboard[1]

    truck_lower = truck[0]
    truck_upper = truck[1]


    if in_interval(truck_lower[0], [billboard_lower[0], billboard_upper[0]]) and in_interval(truck_lower[1], [billboard_lower[1], billboard_upper[1]]):
        x_intersecting = min(abs(billboard_lower[0]-truck_lower[0]), abs(billboard_upper[0]-truck_lower[0]))
        y_interescting = min(abs(billboard_lower[1]-truck_lower[1]), abs(billboard_upper[1]-truck_lower[1]))

    elif in_interval(truck_upper[0], [billboard_lower[0], billboard_upper[0]]) and in_interval(truck_upper[1], [billboard_lower[1], billboard_upper[1]]):
        x_intersecting = min(abs(billboard_lower[0]-truck_upper[0]), abs(billboard_upper[0]-truck_upper[0]))
        y_interescting = min(abs(billboard_lower[1]-truck_upper[1]), abs(billboard_upper[1]-truck_upper[1]))

    else:
        x_intersecting = 0
        y_interescting = 0

    return x_intersecting * y_interescting

def get_area(billboard):
    return(abs(billboard[0][0] - billboard[1][0])*abs(billboard[0][1] - billboard[1][1]))

def in_interval(truck_possible_x_or_y_vals, billboard_x_or_y_bounds):
    if max(billboard_x_or_y_bounds) > truck_possible_x_or_y_vals > min(billboard_x_or_y_bounds):
        return True
    else:
        return False
    
if __name__ == '__main__':
    main()