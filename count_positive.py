def countpositive (somelist):
    count = 0
    for i in range (len(somelist)):
        if somelist[i] > 0:
            count = count + 1
    last_val = len(somelist)-1
    somelist[last_val] = count
    return somelist
print(countpositive([1,3,4,5,-1,-2,3,4,5]))