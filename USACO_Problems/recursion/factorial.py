def factorial(index, currNum):
    if index == 1:
        return currNum
    else:
        return factorial(index - 1, currNum * index)
    
print(factorial(5, 1))