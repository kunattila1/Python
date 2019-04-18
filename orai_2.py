import os
clear = lambda: os.system('cls')
clear() #képernyőtörlés
PI = 3.1415
d = int(input("Kérlek add meg a kör átmérőjét, [cm]-ben!"))
r = d / 2
print("A kör sugara: "+str(r)+" cm")
print("A kör sugara: %f cm" % ( r,))
print("A kör kerülete: {} cm, a kör területe {} ncm".format(d * PI, r * r * PI))
a = float(10)
b = float(3)
print("%d/%d=%d, maradék: %d" % (a,b,a/b,a%b))
input("Nyomj entert a folytatáshoz...")