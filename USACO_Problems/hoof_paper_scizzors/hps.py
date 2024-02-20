import sys

def main():
    
    sys.stdin = open("hps.in", 'r')
    sys.stdout = open("hps.out", 'w')

    num_games = int(input())
    plays_by_FJ = [0]
    for i in range(num_games):
        plays_by_FJ.append(input().strip("\n"))
    
    hooves = [0] * (num_games + 1)
    paper = [0] * (num_games + 1)
    scissors = [0] * (num_games + 1)

    for game in range(1, num_games + 1):
        if plays_by_FJ[game] == "S":
            hooves[game] = hooves[game - 1] + 1
            scissors[game] = scissors[game - 1]
            paper[game] = paper[game - 1]
        elif plays_by_FJ[game] == "P":
            scissors[game] = scissors[game - 1] + 1
            hooves[game] = hooves[game - 1]
            paper[game] = paper[game - 1]
        elif plays_by_FJ[game] == "H":
            paper[game] = paper[game - 1] + 1
            hooves[game] = hooves[game - 1]
            scissors[game] = scissors[game - 1]

    # print(paper)
    # print(hooves)
    # print(scissors)

    max_wins = 0
    for i in range(1, num_games + 1):
        one_half_wins = max(hooves[i], paper[i], scissors[i])
        other_half_wins = max(hooves[-1] - hooves[i], paper[-1] - paper[i], scissors[-1] - scissors[i])
        max_wins = max(max_wins, one_half_wins + other_half_wins)

    print(max_wins)

main()