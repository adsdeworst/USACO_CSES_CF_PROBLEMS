t, c = list(map(int, input().split()))
targets = list(map(int, input().split()))
instructions = input()

hit = 0
current_pos = 0
target_line = [False] * (c + 1 + c)
hits = [0] * (c + 1 + c)
for target in targets:
    target_line[target] = True


for move in instructions:
    if move == "R":
        current_pos += 1
    elif move == "L":
        current_pos -= 1
    else:  # move == 'F'
        if target_line[current_pos]:  # Time: O(1)
            if hits[current_pos] == 0:
                hit += 1
            hits[current_pos] += 1
answer = hit
final_position = current_pos

moves = ["F", "R", "L"]
for old_offset in [-1, 0, +1]:
    old_move = moves[old_offset]
    for new_offset in [-1, 0, +1]:
        new_move = moves[new_offset]
        if old_move != new_move:
            offset = new_offset - old_offset

            hit = 0
            suffix_pos = final_position + offset
            hits = [0] * (c + 1 + c)
            for i in range(c - 1, -1, -1):
                move = instructions[i]
                if move == "R":
                    suffix_pos -= 1
                elif move == "L":
                    suffix_pos += 1
                else:  # move == 'F'
                    if target_line[suffix_pos]:  # Time: O(1)
                        if hits[suffix_pos] == 0:
                            hit += 1
                        hits[suffix_pos] += 1

            # hit = 0
            prefix_pos = 0
            # hits = [0] * (c + 1 + c)
            for i in range(c):
                move = instructions[i]
                # update hits for the current iteration
                # remove move from the suffix
                if move == "R":
                    suffix_pos += 1
                elif move == "L":
                    suffix_pos -= 1
                else:  # move == 'F'
                    if target_line[suffix_pos]:  # Time: O(1)
                        hits[suffix_pos] -= 1
                        if hits[suffix_pos] == 0:
                            hit -= 1

                if move == old_move:
                    # account for the new_move
                    if new_move == "F":
                        if target_line[prefix_pos]:  # Time: O(1)
                            if hits[prefix_pos] == 0:
                                hit += 1
                            hits[prefix_pos] += 1
                    # answer max=simulate(instructions[0..i-1] + new_move + instructions[i+1..c-1])
                    answer = max(answer, hit)
                    # discount the new_move
                    if new_move == "F":
                        if target_line[prefix_pos]:  # Time: O(1)
                            hits[prefix_pos] -= 1
                            if hits[prefix_pos] == 0:
                                hit -= 1

                # update hits for the next iteration (i->i+1)
                if move == "R":
                    prefix_pos += 1
                elif move == "L":
                    prefix_pos -= 1
                else:  # move == 'F'
                    if target_line[prefix_pos]:  # Time: O(1)
                        if hits[prefix_pos] == 0:
                            hit += 1
                        hits[prefix_pos] += 1
print(answer)



# t, c = list(map(int, input().split()))
# targets = list(map(int, input().split()))
# instructions = input()

# hit = 0
# current_pos = 0
# target_line = [False] * (c + 1 + c)
# hits = [0] * (c + 1 + c)
# for target in targets:
#   target_line[target] = True


# for move in instructions:
#   if move == 'R':
#     current_pos += 1
#   elif move == 'L':
#     current_pos -= 1
#   else: # move == 'F'
#     if target_line[current_pos]: # Time: O(1)
#       if hits[current_pos] == 0:
#         hit += 1
#       hits[current_pos] += 1
# answer = hit
# final_position = current_pos

# moves = ['F', 'R', 'L']
# for old_offset in [-1, 0, +1]:
#   old_move = moves[old_offset]
#   for new_offset in [-1, 0, +1]:
#     new_move = moves[new_offset]
#     if old_move != new_move:
#       offset = new_offset - old_offset

#       hit = 0
#       suffix_pos = final_position + offset
#       hits = [0] * (c + 1 + c)
#       for i in range(c - 1, -1, -1):
#         move = instructions[i]
#         if move == 'R':
#           suffix_pos -= 1
#         elif move == 'L':
#           suffix_pos += 1
#         else: # move == 'F'
#           if target_line[suffix_pos]: # Time: O(1)
#             if hits[suffix_pos] == 0:
#               hit += 1
#             hits[suffix_pos] += 1

#       #hit = 0
#       prefix_pos = 0
#       #hits = [0] * (c + 1 + c)
#       for i in range(c):
#         move = instructions[i]
#         # update hits for the current iteration
#         # remove move from the suffix
#         if move == 'R':
#           suffix_pos += 1
#         elif move == 'L':
#           suffix_pos -= 1
#         else: # move == 'F'
#           if target_line[suffix_pos]: # Time: O(1)
#             hits[suffix_pos] -= 1
#             if hits[suffix_pos] == 0:
#               hit -= 1

#         if move == old_move:
#           # account for the new_move
#           if new_move == 'F':
#             if target_line[prefix_pos]: # Time: O(1)
#               if hits[prefix_pos] == 0:
#                 hit += 1
#               hits[prefix_pos] += 1
#           #answer max=simulate(instructions[0..i-1] + new_move + instructions[i+1..c-1])
#           answer = max(answer, hit)
#           # discount the new_move
#           if new_move == 'F':
#             if target_line[prefix_pos]: # Time: O(1)
#               hits[prefix_pos] -= 1
#               if hits[prefix_pos] == 0:
#                 hit -= 1

#         # update hits for the next iteration (i->i+1)
#         if move == 'R':
#           prefix_pos += 1
#         elif move == 'L':
#           prefix_pos -= 1
#         else: # move == 'F'
#           if target_line[prefix_pos]: # Time: O(1)
#             if hits[prefix_pos] == 0:
#               hit += 1
#             hits[prefix_pos] += 1
# print(answer)

