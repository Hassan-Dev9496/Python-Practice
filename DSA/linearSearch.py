# Showing Message if elment is find

# def linear_search(arr , item):
#     for i in range(len(arr)):
#         if item == arr[i]:
#          return f"The number is found is index : {i} "
#     return f"The number {item} is not found in the list"

# arr =['1' , '2' , '3' , '4' , '5']
# item='10'


# print(linear_search(arr , item))


#return that searched element and place the searched in zero index method 1

# def linear_search(arr , item):
#     for i in range(len(arr)):
#         if arr[i] == item:
#             temp = arr[0]
#             arr[0] = arr[i]
#             arr[i] = temp
#             return arr
#     return -1 
        

# arr =['1' , '2' , '3' , '4' , '5']
# item='5'

# result = linear_search(arr , item)
# print(result)


#return that searched element and place the searched in zero index method 2

# def linear_search(arr , item):
#     for i in range(len(arr)):
#         if arr[i] == item:
#             arr[0] , arr[i] = arr[i] , arr[0]
#             return arr
#     return -1 
        

# arr =['1' , '2' , '3' , '4' , '5']
# item='5'

# result = linear_search(arr , item)
# print(result)

#linear search in method


# def liner_search(arr , item):
#     if item in arr:
#         print("Yes item is in array")
#     else:
#         print("No")

# arr =['1' , '2' , '3' , '4' , '5']
# item='3'

# liner_search(arr , item)

#find max number in array 

# def linear_search (arr):
#     for i in range(len(arr)):
#         highest = arr[0]
#         if arr[i] > highest:
#             highest = arr[i]
#     return highest

# arr =['1' , '2' , '3' , '4' , '5']

# print(linear_search(arr))  

#repeating element

# def linear_search(array):
#     visited= set()
    
#     for num in array:
#         if num in visited:
#             first_repeating = num
#         else:
#             visited.add(num)

#     return first_repeating
            
# arr =[1 , 2 , 3 , 3 , 4, 5]
# print(linear_search(arr))  


#find the occurance of numbers greater than target
def linear_search(array , target):
    visited = set()
    for num in array:
        if num > target:
            visited.add(num)
    return len(visited)

arr =[1 , 2 , 3 , 4, 5]
target = 2
print(linear_search(arr , target))  












