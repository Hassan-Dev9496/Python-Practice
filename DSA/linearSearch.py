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


def liner_search(arr , item):
    if item in arr:
        print("Yes item is in array")
    else:
        print("No")

arr =['1' , '2' , '3' , '4' , '5']
item='3'

liner_search(arr , item)










