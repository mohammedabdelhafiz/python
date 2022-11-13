def minimum(theminlist):
    if len(theminlist) == 0:
            return False
    else:
            min = theminlist[0]
            for i in range (len(theminlist)):
                if theminlist[i] < min:
                    min=theminlist[i]
            return min

print(minimum([37,2,1]))

def sum_array(lissst):
    sum = 0
    for i in range (len(lissst)):
        sum = sum + lissst[i]
    return sum

print (sum_array([1,5,9,8,-1,-5]))


def max(theminlist):
    if len(theminlist) == 0:
            return False
    else:
            max = theminlist[0]
            for i in range (len(theminlist)):
                if theminlist[i] > max:
                    max=theminlist[i]
            return max

print(max([37,2,1,-9]))

def length(len_list):
    return len(len_list)

print(len([]))


def bigdata(thebiglist):
    sum = sum_array(thebiglist)
    min = minimum(thebiglist)
    max = max(thebiglist)
    avg = sum_array(thebiglist)
    len = length(thebiglist)

    bigdata = {
        'sumtotal' : sum,
        'minimum' : min,
        'maximum' : max,
        'average' : avg,
        'length' : len
    }

    return bigdata