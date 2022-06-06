q= int(input("How much items are you buying? "))
y = 0
for w in range(0,q):
    e = input("What item are you purchasing? ")
    r = float(input("How much? "))
    print("Thanks for puchasing "+ e)
    y = y + r   
print("Your total is : " + str(y))
print("Have a nice day!")
