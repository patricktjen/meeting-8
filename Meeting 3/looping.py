# for loop
# 1 parameter
print("1 parameter")
for i in range(10):
    print(i)

# 2 parameter (start,end)
print("2 parameter")
for i in range(10,16):
    print(i)

# 3 parameter (start,end,jump)
print("3 parameter")
for i in range(16,26,2):
    print(i)

print("reversed 3 parameter")
for i in range(30,0,-2):
    print(i)

# while loop
x = 1
while x<=5:
    print(x)
    x = x+1
print("selesai")

# enhanced for loop (loop all, cannot select)
fruits = ["banana","melon","coconut"]
for x in fruits:
    print(x)

# continue
print("ini continue")
for i in range(5):
    if i == 3:
        continue    #langsung lanjut loop
    else:
        print("bukan 3")

# break
print("ini break")
for i in range(5):
    if i == 3:
        break       #langsung stop loop
    else:
        print(i)

