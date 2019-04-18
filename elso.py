
#c = 10000
#r = 0.08
#m = 12
#valami = input("Add meg az évek számát: ")
#t = int(valami)
#fv = c*(1+r/m)**(m*t)
#print(fv)

x = int(input("Give the year: "))
if x % 4 == 0 and x % 100 != 0 or x % 400 == 0:
    print("It's a leap year")
else:
    print("It's just a common year")

