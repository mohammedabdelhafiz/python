

def pos (biggie_size):
    for x in range (len(biggie_size)):
        if biggie_size[x] > 0 :
            biggie_size[x] = "big"
    return biggie_size 
print(pos([-1,-4,4,5,6,7,8]))


def pom(listtat):
    for i in range (len(listtat)):
        if listtat [i] > 0:
            listtat[i] = "BIG"
    return listtat

print(pom([1,3,4,5,6,7,-1,-9,-6]))


def fuun(thebiglist):
    for m in range (len(thebiglist)):
        if thebiglist[m] > 0 :
            thebiglist[m] = "HAHA"
    return thebiglist
print(fuun([1,4,7,-1,-5,4,-9,8]))

