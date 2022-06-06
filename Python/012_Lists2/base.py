import random
q = int(input("How many random numbers? "))
thislist = [1,2,3,4,5,6,7,8,9,0]
for w in range(0,q):
    e = random.randrange(10)
    print(thislist[e])
