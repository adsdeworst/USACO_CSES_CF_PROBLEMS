hierarchy = [4, 5, 6]
strict_ord = [[5, 3], [3, 1]]

result = [0] * 6

for i in strict_ord:
    result[i[1]] = i[0]

print(result)

for i in range(len(result)):
    if result[i] in hierarchy:
        place_in_hierarchy = hierarchy.index(result[i]) # where in hierarchy its located
        place_in_result = i # where in result
        result[i-place_in_hierarchy-1:i] = hierarchy[0:place_in_hierarchy]
    
print(result)
