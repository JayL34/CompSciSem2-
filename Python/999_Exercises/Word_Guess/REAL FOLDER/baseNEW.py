import random
a =0
w =0
thislist =[]
with open('allow_words.txt') as f:
    for line in f:
        l = line.strip()
        thislist.append(l)
q = thislist[random.randrange(12972)]
print(q)
b = 0
for w in range(w,6):
    e = input("Try to guess the 5 letter word : ")
    if e == q:
        print("correct you are right")
        b = 1
        break
    elif e != q:
        for r in thislist:
            if e == r:
                a = 1 
        if a == 1:
            print("You are wrong.")
            w=w+1
        else: 
            print("That is not in the list. Try agian")
            
        a=0
if b == 0:
    print("You lost, answer was " +q)
f.close()
