person = {
    "name":"patrick",
    "age":18,
    "hobby":"football"
    }

print(person)

# access data
print(person["name"])
print(person["age"])
print(person["hobby"])

# update data
person["name"] = "dybala"
print(person)

person["city"] = "buenos aires"
print(person)

# delete data
# langsung hapus
del person["hobby"]
print(person)

# pop data
# ambil data sebelum dihapus
city = person.pop("city")
print("Data yang dihapus adalah:", city)
print(person)

# list in dictionary
person['cars'] = ["audi","lamborghini"]
print(person)
print(person['cars'][0])

# dictionary in dictionary
person['address'] = {
    'street':"Bakerville",
    'number':21
}
print(person)
print(person['address']['street'])

# print all keys
print(person.keys())
print(person.values())
print(person.items())

# convert keys to list
list_key = list(person.keys())
print(list_key)

# convert values to list
list_values = list(person.values())
print(list_values)

# convert items to list
list_items = list(person.items())
print(list_items)