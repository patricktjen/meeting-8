import random 

def random_arr(length,min_value,max_value):
    arr = []
    for value in range(length):
        random_value = random.randint(min_value,max_value)
        arr.append(random_value)
    return arr

def quick(arr):
    def _quick(arr,low,high):
        if low < high:
            pi = partition(arr,low,high)
            _quick(arr,low,pi-1)
            _quick(arr,pi+1,high)

    def partition(arr,low,high):
        pivot = arr[high]
        i = low-1
        for j in range(low,high):
            if arr[j]<= pivot:
                i+=1
                arr[i],arr[j] = arr[j],arr[i]

        arr[i+1],arr[high] = arr[high],arr[i+1]
        return i+1
    
    _quick(arr,0,len(arr)-1)

arr = random_arr(100000,0,20)
print("order before data is sorted: ")
for i in range(len(arr)):
    print("%d" % arr[i], end=' ')
print()

quick(arr)
print("order after data is sorted: ")
for i in range(len(arr)):
    print("%d" % arr[i], end=' ')