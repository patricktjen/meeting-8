nama = "patrick"
umur = "18"
hobi = "golf"

# string formatting
## positional argument
print("Nama saya {0} dan saya berumur {1} hobi saya adalah {2}".format(nama,umur,hobi))

## keyword argument
print("Nama saya {name} dan saya berumur {age}. Hobi saya adalah {hobby}".format(name=nama,age=umur,hobby=hobi))
print("Nama saya {} dan saya berumur {} hobi saya adalah {}".format(nama,umur,hobi))