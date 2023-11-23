input = [1, 2, 3, 4]
res = []
def sub(l):
    if l == []:
        return []
    else:
        res.append(l)
        sub(l[0:])
    
sub(input)
print(res)