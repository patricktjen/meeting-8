import random 

def random_arr(length,min_value,max_value):
    arr = []
    for value in range(length):
        random_value = random.randint(min_value,max_value)
        arr.append(random_value)
    return arr 

def bubble(arr):
    n = len(arr)
    # lakukan pertukaran sebanyak n-1 kali
    for i in range(n):
        # lakukan pertukaran sebanyak n-i-1 kali
        for j in range(0, n-i-1):
            # jika element saat ini lebih besar daripada element selanjutnya
            if arr[j] > arr[j+1]:
                # tukar posisi element
                arr[j], arr[j+1] = arr[j+1], arr[j] 


arr = random_arr(20,0,20)
print("order before data is sorted: ")
for i in range(len(arr)):
    print("%d" % arr[i], end=' ')
print()

bubble(arr)
print("order after data is sorted: ")
for i in range(len(arr)):
    print("%d" % arr[i], end=' ')