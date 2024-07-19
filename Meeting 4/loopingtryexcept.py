# string dipetik ""
# character dipetik '
# string tidak bisa dipangkatkan
angka = [1,2,"three",4,5]
print("angka pangkat")
for num in angka:
    try:
        print(num)
    except TypeError :
        print(f"Tipe data berbeda {num}")
    