def get_max_area(triangle_coords): 
    max_y = 0
    max_x = 0
    for i in range(len(triangle_coords)):
        for j in range(i+1, len(triangle_coords)):
            if triangle_coords[i][0] == triangle_coords[j][0]:
                if abs(triangle_coords[i][1] - triangle_coords[j][1]) > max_y:
                    max_y = abs(triangle_coords[i][1] - triangle_coords[j][1])
            if triangle_coords[i][1] == triangle_coords[j][1]:
                if abs(triangle_coords[i][0] - triangle_coords[j][0]) > max_x:
                    max_x = abs(triangle_coords[i][0] - triangle_coords[j][0])
    
    return max_x * max_y

def main():
    with open("triangles.in", "r") as f:
        n = int(f.readline())
        post_coords = []
        for _ in range(n):
            post_coords.append(list(map(int, f.readline().split())))
        max_area = 0

    for a in range(len(post_coords)):
        for b in range(a+1, len(post_coords)):
            for c in range(b+1, len(post_coords)):
                triangle_coords =  [post_coords[a], post_coords[b], post_coords[c]]
                area = get_max_area(triangle_coords)
                if area  > max_area:
                    max_area = area
    
    with open("triangles.out", "w") as f:
        f.write(str(max_area))

if __name__ == "__main__":
    main()