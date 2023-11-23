def intersecting_area(billboard, truck):
    lower_billboard_choords = billboard[0]
    upper_billboard_choords = billboard[1]

    lower_truck_choords = truck[0]
    upper_truck_choords = truck[1]

    if (lower_billboard_choords[1] > upper_truck_choords[1] and
        lower_truck_choords[1] > upper_billboard_choords[1] and
        upper_billboard_choords[0] > lower_truck_choords[0] and
        upper_truck_choords[0] > lower_billboard_choords[0]):
        return abs(lower_billboard_choords[0] - upper_billboard_choords[0]) * abs(lower_billboard_choords[1] - upper_billboard_choords[1])
    
    else:
        answer_a = 0
        answer_a = abs(upper_billboard_choords[1] - lower_truck_choords[1]) * abs(upper_billboard_choords[0] - lower_truck_choords[0]) 
        return answer_a
    

def main():
    with open("billboards.in", "r") as f:
       billboard_a =  list(map(int, f.readline().strip("\n").split()))
       billboard_a = [(billboard_a[0], billboard_a[1]), (billboard_a[2], billboard_a[3])]

       billboard_b = list(map(int, f.readline().strip("\n").split()))
       billboard_b = [(billboard_b[0], billboard_b[1]), (billboard_b[2], billboard_b[3])]

       truck = list(map(int, f.readline().strip("\n").split()))
       truck = [(truck[0], truck[1]), (truck[2], truck[3])]
       print(str(intersecting_area(billboard_a, truck) + intersecting_area(billboard_b, truck))) 
    
    with open("billboards.out", "w") as f:
        f.write(str(intersecting_area(billboard_a, truck) + intersecting_area(billboard_b, truck)))

main()