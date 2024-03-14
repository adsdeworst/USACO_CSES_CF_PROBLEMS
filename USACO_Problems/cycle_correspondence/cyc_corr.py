n, k = list(map(int, input().split()))
list_a = list(map(int, input().split()))
list_b = list(map(int, input().split()))

offset = []

included = [False] * (1 + n) # could be made better
not_inc = 0

for i in range(k): # could be made better
    included[list_a[i]] = True 
    included[list_b[i]] = True
    
for i in range(1, 1 + n): # could be made better
    if not included[i]:
        not_inc += 1

for i in range(k):
    if list_a[i] in list_b: # append 0?
        if list_b.index(list_a[i]) - i < 0:
            offset.append(list_b.index(list_a[i]) - i + k)
        else:
            offset.append(list_b.index(list_a[i]) - i)

length = len(offset)
offset_counts = []
count = 0        
if length != 0:
    for i in range(length - 1):
        if offset[i] == offset[i + 1]:
            count += 1
        else:
            count += 1
            offset_counts.append(count)
            count = 0
    count += 1
    offset_counts.append(count)
    count = 0
    answer = not_inc + max(offset_counts)
else:
    answer = 0


list_a = list(reversed(list_a))
offset = [] 

for i in range(k):
    if list_a[i] in list_b:
        if list_b.index(list_a[i]) - i < 0:
            offset.append(list_b.index(list_a[i]) - i + k)
        else:
            offset.append(list_b.index(list_a[i]) - i)
        
        
offset.sort()
length = len(offset)
offset_counts = []
count = 0
if length != 0:
    for i in range(length - 1):
        if offset[i] == offset[i + 1]:
            count += 1
        else:
            count += 1
            offset_counts.append(count)
            count = 0
    count += 1
    offset_counts.append(count)
    count = 0
    answer = max(answer, not_inc + max(offset_counts))
else:
    answer = 0
    
print(answer)

# n, k = list(map(int, input().split()))
# list_a = list(map(int, input().split()))
# list_b = list(map(int, input().split()))

# offset = []

# included = [False] * (1 + n)
# answer = 0

# for i in list_a:
#     included[i] = True
    
# for i in list_b:
#     included[i] = True

# for i in range(k):
#     if list_a[i] in list_b:
#         if list_b.index(list_a[i]) - i < 0:
#             offset.append(list_b.index(list_a[i]) - i + k)
#         else:
#             offset.append(list_b.index(list_a[i]) - i)
#--------------------            
# offset_counts = []
# count = 0        
# if len(offset) != 0:
#     for i in range(len(offset) - 1):
#         if offset[i] == offset[i + 1]:
#             count += 1
#         else:
#             count += 1
#             offset_counts.append(count)
#             count = 0
#     count += 1
#     offset_counts.append(count)
#     count = 0
#-------------
# offset = []            
# list_a = list(reversed(list_a))
# for i in range(k):
#     if list_a[i] in list_b:
#         if list_b.index(list_a[i]) - i < 0:
#             offset.append(list_b.index(list_a[i]) - i + k)
#         else:
#             offset.append(list_b.index(list_a[i]) - i)
        
# for i in range(1, 1 + n):
#     if not included[i]:
#         answer += 1
# offset.sort()

# offset_counts = []
# count = 0
# if len(offset) != 0:
#     for i in range(len(offset) - 1):
#         if offset[i] == offset[i + 1]:
#             count += 1
#         else:
#             count += 1
#             offset_counts.append(count)
#             count = 0
#     count += 1
#     offset_counts.append(count)
#     count = 0
#     print(answer + max(offset_counts))
# else:
#     print(0)