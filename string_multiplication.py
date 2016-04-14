

def add(c1, c2):
    return str(int(c1) + int(c2))

def mult(c1, c2):
    return str(int(c1) * int(c2))

def strmult(s1, s2):
    sum_list = []
    for i in range(len(s2)):
        temp_sum = mult(s1, s2[i])
        new_sum = temp_sum + (len(s2)- i - 1) * '0'
        sum_list.append(new_sum)
    sum_of_ele = 0
    for x in sum_list:
        sum_of_ele = add(sum_of_ele, x)
    
    return sum_of_ele
        
        
s1 = "1234"
s2 = "5678"
print(strmult(s1, s2))

