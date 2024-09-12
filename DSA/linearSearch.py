# Showing Message if elment is find

def linear_search(arr , item):
    for i in range(len(arr)):
        if item == arr[i]:
         return f"The number is found is index : {i} "
    return f"The number {item} is not found in the list"

arr =['1' , '2' , '3' , '4' , '5']
item='10'


print(linear_search(arr , item))







