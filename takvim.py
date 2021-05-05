import calendar
import sys

print("------------------")

try:
    yıl = int(input("Yıl giriniz: "))
except:
    print("Bir hata ile karşılaşıldı. Lütfen yıl değerini, geçerli bir değer olarak giriniz.")    
    sys.exit()
try:
    ay = int(input("Ay Giriniz: "))
except:
    print("Bir hata ile karşılaşıldı. Lütfen ay değerini, geçerli bir değer olarak giriniz.")   
    sys.exit()     
    
print("------------------ \n")


print("-------------------------- \n")

try:
    print(calendar.month(yıl, ay))
except:
    print("Bir hata ile karşılaşıldı. Lütfen söz konusu yıl ve ay değerlerini, geçerli bir değer olarak girdiğinizden emin olunuz.")   
    print("--------------------------")
    sys.exit()         


print("--------------------------")
