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


