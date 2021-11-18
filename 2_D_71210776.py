#Soal 2
a = int(input("Nilai a : "))
b = int(input("Nilai b : "))
c = int(input("Nilai c : "))

D = b**2 - 4*a*c 
x = (-b-((b**2)-(4*a*c))**0.5)/2*a
y = (-b+((b**2)-(4*a*c))**0.5)/2*a

if D < 0 :
    print("Fungsi tersebut tidak memiliki akar riil")
elif D > 0 :
    print("Akar akar dari persamaan tersebut adalah ", x, "dan", y)
elif D == 0 :
    print("Fungsi tersebut memiliki akar kembar yaitu ", x)