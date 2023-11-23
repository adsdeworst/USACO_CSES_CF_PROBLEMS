import datetime
dt = datetime.datetime.now()

def go_back(index, val):
    index = index - val
    return index

def sum_list(list):
    sum = 0
    for all in list:
        sum += all
    return sum

def main():
    with open('censor.in', 'r') as f:
        S = f.readline().strip("\n")
        censor_string = f.readline()
        answer_string = ""
        occurences_list = []
    index = 0
    while index != len(S):
        if (S[index] in censor_string) == True:
            #do someting
            exactment_factor = 0
            for i in range(len(censor_string)):
                if censor_string[i] == S[index+i]:
                    exactment_factor += 1
                    if exactment_factor == len(censor_string):
                       S = S[0:index] + S[index+len(censor_string):len(S)]
                       if len(occurences_list) != 0:
                            index = go_back(index, occurences_list[len(occurences_list)-1])
                            occurences_list.pop(len(occurences_list) - 1) 
                            break
                       else:
                           occurences_list=[]
                else:
                    occurences_list.append(exactment_factor)
                    index += i
                    break
        else:
            if len(occurences_list) != 0:
                answer_string += S[index-sum_list(occurences_list):index]
                occurences_list=[]
            answer_string += S[index]
            index += 1
    print(answer_string)
main()
dx = datetime.datetime.now()
print(dt.microsecond/1000 - dx.microsecond/1000)
