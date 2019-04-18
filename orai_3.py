import os
clear = lambda: os.system('cls')
clear() #képernyőtörlés
class szamologep:
    def szorzas(n):
        m = int(input("Add meg, hogy mennyivel szeretnél szorozni: "))
        print("%d * %d = %d" % (n,m,n*m))
    def osztas(n):
        m = int(input("Add meg, hogy mennyivel szeretnél osztani: "))
        print("%d / %d = %d" % (n,m,n/m))
    def kivonas(n):
        m = int(input("Add meg, hogy mennyit szeretnél kivonni: "))
        print("%d - %d = %d" % (n,m,n-m))
    def osszeadas(n):
        m = int(input("Add meg, hogy mennyit szeretnél hozzáadni: "))
        print("%d + %d = %d" % (n,m,n+m))
    def modusz(n):
        m = int(input("Add meg, hogy mennyivel szeretnél osztani, a végén kiírom neked a maradékot: "))
        print("%d mod %d = %d" % (n,m,n%m))
    def feldolgoz():
        n = int(input("Adj meg egy számot: "))
        choice = input("Szorozni, osztani, kivonni vagy összeadni akarsz vagy az osztás maradékát megnézni? ")
        while choice not in (keywords):
            choice = input("Szorozni, osztani, kivonni vagy összeadni akarsz vagy az osztás maradékát megnézni? ")
        if choice == "szorozni": szamologep.szorzas(n)
        elif choice == "osztani": szamologep.osztas(n)
        elif choice == "kivonni": szamologep.kivonas(n)
        elif choice == "összeadni": szamologep.osszeadas(n)
        elif choice == "az osztás maradékát megnézni": szamologep.modusz(n) 
print("Számológép by Kun Attila 2019.04.15.")
keywords = ["szorozni", "osztani","kivonni","összeadni","az osztás maradékát megnézni"]
end = "nem"
while end != "igen":
    szamologep.feldolgoz()
    end = input("szeretnéd a programot bezárni? (igen/nem): ")
    
    
