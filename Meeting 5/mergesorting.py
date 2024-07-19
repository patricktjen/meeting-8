import random 

def random_arr(length,min_value,max_value):
    arr = []
    for value in range(length):
        random_value = random.randint(min_value,max_value)
        arr.append(random_value)
    return arr

def merge(arr):
    if (len(arr))> 1:
        mid = (len(arr)) // 2
        left = arr[:mid]
        right = arr[mid:]
        
        merge(left)
        merge(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i+=1
            else:
                arr[k] = right[j]
                j+=1
            k+=1

        while i < len(left):
            arr[k] = left[i]
            i+=1
            k+=1

        while j < len(right):
            arr[k] = right[j]
            j+=1
            k+=1

arr = random_arr(10,0,20)
print("order before data is sorted: ")
for i in range(len(arr)):
    print("%d" % arr[i], end=' ')
print()

merge(arr)
print("order after data is sorted: ")
for i in range(len(arr)):
    print("%d" % arr[i], end=' ')
