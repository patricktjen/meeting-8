#set
numbers = {3,5,4,1,2}
print(numbers)

mahasiswa = {"patrick", "galen", "ferrel","jobel"}
print(mahasiswa)

# add data to set
mahasiswa.add("ole")
mahasiswa.add("fayola")
mahasiswa.add("fayola")
mahasiswa.add("fayola")
print(mahasiswa)

# remove data from set (hapus kalau ada, kalau gaada error)
mahasiswa.remove("ole")
print(mahasiswa)

# discard (hapus kalau ada, kalau gaada gapapa)
mahasiswa.discard("josh")
print(mahasiswa)