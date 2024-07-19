import random 

def random_arr(length,min_value,max_value):
    arr = []
    for value in range(length):
        random_value = random.randint(min_value,max_value)
        arr.append(random_value)
    return arr

def selection(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i],arr[min_idx] = arr[min_idx],arr[i]

        temp = arr[i]
        arr[i] = arr[min_idx]
        arr[min_idx] = temp

arr = random_arr(20,0,20)
print("order before data is sorted: ")
for i in range(len(arr)):
    print("%d" % arr[i], end=' ')
print()

selection(arr)
print("order after data is sorted: ")
for i in range(len(arr)):
    print("%d" % arr[i], end=' ')