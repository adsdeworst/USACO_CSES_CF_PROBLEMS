# Name: Air Cownditioning
# Link: http://www.usaco.org/index.php?page=viewproblem2&cpid=1276


# 2 9 2 3
# 1 6 2 8
# 1 2 4 2
# 6 9 1 5
        

import sys

def main():
    conditioners = {1 : [1, 2, 4, 2], 2 : [2, 9, 2, 3], 3 : [6, 9, 1, 5], 4 : [1, 6, 2, 8]}
    conditioners_index = [1, 2, 3, 4]

def make_perm:
    # if conditioners cool all the cows by the right amount, return
    # else continue with next combination
    if all_cooled() == True:
        # do stuff
    else:
        for i in range(len(conditioners)):


def all_cooled(conditioners, cows):
    # if cows in all the intervals are sufficiently cooled \
    for cow in range(len(cows)):
        for conditioner in range(len(conditioners)):
            