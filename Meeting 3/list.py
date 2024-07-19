fruits = ["apple", "banana", "mango"]

print(fruits) 

# indexing
print(fruits[2])
print(fruits[0])
print(fruits[1])
print(fruits[-1]) # -1 ambil data paling belakang, -2, -3, dst.

# append (menambah element di akhir list)
fruits.append("avocado")
fruits.append("mangosteen")
print(fruits)

# insert (untuk nambah data di index tertentu)
fruits.insert(3, "cherry")
print(fruits)

# remove (hapus berdasarkan value)
fruits.remove("mango")
print(fruits)

# pop (menghapus elemen berdasarkan index)
fruits.pop(3)
print(fruits)

# list indexing (mengubah element pada list)
fruits[3] = "soursop"
print(fruits)

# merge
veggies = ["carrot", "spinach"]
bucket = fruits + veggies
print(bucket)

# slicing
print(bucket[1:4])
print(bucket[2: ])
print(bucket[ :4])

# list in a list
lemari = [["apple","banana"],["carrot","spinach"]]
print(lemari)
print(lemari[0])
print(lemari[0][1])

print(bucket)
bucket.append("mango")
print(bucket)

# list sorting
bucket.sort()
print(bucket)