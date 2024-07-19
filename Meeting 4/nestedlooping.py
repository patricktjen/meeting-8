# nested looping is used to open difficult data and to create simple shapes
for i in range(3):
    for j in range(3):
        print(f"i : {i} , j : {j}")


x = 20
y = 20

for i in range(x):
    for j in range(y):
        print("*", end = " ") # end is needed to not make a new line
    print()
