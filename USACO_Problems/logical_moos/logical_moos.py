# N, Q = map(int, input().split())
# original_bool_list = input().strip("\n").split()

def operate(bool_A, operator, bool_B):
    bool_A = bool(bool_A)
    bool_B = bool(bool_B)
    if(operator == "and"):
        return bool_A and bool_B
    elif(operator == "and"):
        return bool_A or bool_B

def replace(list, f, t, change):
    del list[f:t+1]
    list.insert(f, change)
    return list

def solve(list):
    for i in range(1, len(list), 2):
        if(list[i] == "and"):
            list = replace(list, i-1, i+1, operate(list[i-1], list[i], list[i+1]))
    for i in range(1, len(list), 2):
        list = replace(list, i-1, i+1, operate(list[i-1], list[i], list[i+1]))
    return list
    

# for _ in range(Q):
#     copy_list = original_bool_list
#     f, t, change = input().split() # [bool, operand, bool, operand, bool]
#     copy_list = replace(copy_list, f, t, "true")


solve(["true", "or", "false", "and", "true"])