def check_if_contains_avg_flower(flower_list, i, j):
    photo_list = [flower_list[i:j]]
    average = sum(photo_list)/len(photo_list)
    if (average in photo_list) is True:
        return 1
    else:
        return 0
    
def main():
    with open('daisy_chain.txt', 'r') as f:
        N = int(f.readline([0]))
        flower_list = map(int, f.readlines([1]).split())
    answer = 0
    for i in range(N):
        for j in range(N):
            answer += check_if_contains_avg_flower(flower_list, i, j)
    return answer

main()