import bisect

arr = [1, 3, 4, 4, 5, 7]
x = 4

index_left = bisect.bisect_left(arr, x)  
index_right = bisect.bisect_right(arr, x) 

print(index_left)