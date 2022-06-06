q =int(input("Enter line length : "))
w = input("Horizontal or Verical :  ")
if w == 'horizontal' :
    for x in range(0,q):
        print("*", end= "")
elif w == 'vertical' :
    for z in range(0,q) :
        print("*")
elif w == 'Horizontal' :
    for x in range(0,q):
        print("*", end= "")
elif w == 'Vertical' :
    for z in range(0,q) :
        print("*")
