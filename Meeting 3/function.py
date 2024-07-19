# function without parameter
def greet():                # define
    print("Buenos dias!")
greet()                     # invoke function

# function with parameter
def kenalan(nama, umur):
    print(f"Halo, nama saya {nama} dan saya berumur {umur}")
kenalan("drogba", 22)
kenalan("zidane", 28)

# function with return value
def jumlahkan(a,b):
    return a+b

x = jumlahkan(10,5)
y = jumlahkan(187,290)
print(x+y)

def kenalan2(nama, umur):
    return f"Halo, nama saya {nama} dan saya berumur {umur}"
x = kenalan("drogba", 22)
y = kenalan("zidane", 28)

# function with default parameter
def greeting(nama ="vlahovic"):
    print(f"Terima kasih atas pembeliannya {nama}")

greeting()
greeting("mckennie")

# fungsi lambda
# x = lambda a : a * 10
# print (x(5))

def volume_tabung(jari,tinggi):
    return (3.14 * jari * jari * tinggi)

print(volume_tabung(0.5,2))




