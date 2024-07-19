file = open("contoh_list.txt","r")
content = file.read()
print(content)
file.close()

file = open("contoh_list.txt","r")
content = file.readline()
print(content)
file.close()

file = open("contoh_list.txt","r")
content = file.readlines()
print(content)
file.close()

