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
