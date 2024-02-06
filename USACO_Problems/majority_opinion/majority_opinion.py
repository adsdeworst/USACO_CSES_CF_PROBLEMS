import collections

def main():
    n = int(input())
    for _ in range(n):
        cows = int(input().strip("\n"))
        hay_favorites = list(map(int, input().strip("\n").split()))
        all_possib = []
        if cows == 1:
            print(hay_favorites[0])
        elif (cows == 2) and (hay_favorites[0] == hay_favorites[1]):
            print(hay_favorites[0])
        elif (cows == 2) and (hay_favorites[0] != hay_favorites[1]):
            print(-1)

        if cows > 2:
            for i in range(cows - 2):
                three_fav = hay_favorites[i: i + 3]
                for k in range(3):
                    if three_fav.count(three_fav[k]) >= 2:
                        if not(three_fav[k] in all_possib):
                            all_possib.append(three_fav[k])
            if len(all_possib) == 0:
                print(-1)
            else:
                all_possib.sort()
                print(" ".join(map(str, all_possib)))

main()