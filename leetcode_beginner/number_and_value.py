


def removeElement(number, val):
    j = 0
    for i in range(len(number)):
        if number[i] != val:
            number[j] = number[i]
            j += 1
        
    return j 



number = [0,1,2,2,3,0,4,2]

print(removeElement(number, 2)) 

