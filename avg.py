def sum_array(lissst):
    sum = 0
    for i in range (len(lissst)):
        sum = sum + lissst[i]
    return sum/len(lissst)

print (sum_array([1,2,3,4]))
