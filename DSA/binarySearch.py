def binary_search(arr , target):
    left , right = 0 , len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return target
        elif arr[mid] > target:
            right = mid - 1
        else:
            arr[mid] < target
            left = mid + 1

arr = ["10" , "40" , "50" , "80" , "100"]
target="40"
print(binary_search(arr ,target ))


#funtion which sorts the array first using selection sort and then find the target 

def binearySearch(array , target):
    left , right = 0 , len(arr) - 1
    while left <= right:
        mid =(left + right) // 2
        if array[mid] == target:
            return target
        elif array[mid] > target:
            right = mid-1
        else:
            array[mid] < target
            left = mid+1

def selection_sorting(array):
    n=len(array)
    for i in range(n-1):
        least = i
        for j in range(i+1 , n):
            if array[j] < array[least]:
                least = j
        array[i] , array[least] = array[least] , array[i]
    return array


arr = [15 , 30 , 10 , 8 , 20 , 1]
target = 8
sorted_array = selection_sorting(arr)
result = binearySearch(sorted_array , target)
print(result , "result")



