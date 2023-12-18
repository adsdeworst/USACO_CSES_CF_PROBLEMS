def main():
    file_input = open("USACO_Problems\\sleepy_cow_herding\\herding.in", "r")
    file_output = open("USACO_Problems\\sleepy_cow_herding\\herding.out", "w")

    places = file_input.readline().strip("\n").split()
    places = list(map(int, places))
    file_output.writelines(str(check_min(places)) + "\n")
    file_output.writelines(str(check_max(places)))


def check_min(current_places):
    if current_places[2] - current_places[1] == 2 or current_places[0] - current_places[1] == 2:
        return 1
    elif sorted(current_places) == current_places:
        return 0
    return 2

def check_max(current_places):
    count = 0
    while current_places[1] - current_places[0] != current_places[2] - current_places[1] != 1:
        # num = current_places[2]
        current_places[2] = current_places[0] + 1
        current_places = sorted(current_places)
        current_places[0] = current_places[2] - 1
        current_places = sorted(current_places)
        count += 2
    
    return count

if __name__ == "__main__":
    main()