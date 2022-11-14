import random
def randInt(min=0   , max=1   ):
    num = random.random()
    return num
#print(randInt()) 		    # should print a random integer between 0 to 100
#print(randInt(max=50)) 	    # should print a random integer between 0 to 50
#print(randInt(min=50)) 	    # should print a random integer between 50 to 100
#print(randInt(min=50, max=500))    # should print a random integer between 50 and 500

print(randInt()) 

def randInt_two( min=0   , max=100 ):
    num = random.randint(0,100) # should print a random integer between 0 to 100
    return num
print(randInt_two())


import random
def randInt(max=100):
    num = random.random()
    return num

print(randInt(max=50))