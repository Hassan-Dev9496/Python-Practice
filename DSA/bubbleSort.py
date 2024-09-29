def bubble_sorting(array):
    n=len(array)
    for i in range(n):
        swapped= False
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j] , array[j+1] = array[j+1] , array[j]
                swapped = True
        if not swapped:
            break
    return array


array = [1,2,3,4,5]
print(bubble_sorting(array))

#Sorting Alphabets and removing duplicate

def dubplicate_checker(list_of_name):
    visited=[]
    for i in range(len(list_of_name)):
        if list_of_name[i] not in visited:
            visited.append(list_of_name[i])
    return visited 

def bubble_sorting_alphabets(name):
    list_of_name= list(name)
    size = len(list_of_name)
    visited = set()
    for i in range(size):
        swapped = False
        for j in range(0, size-i-1):
            visited.add(list_of_name[j])
            if list_of_name[j] > list_of_name[j+1]:
                list_of_name[j] , list_of_name[j+1] = list_of_name[j+1] , list_of_name[j]
                swapped = True
        if not swapped:
            break
    return dubplicate_checker(list_of_name)


name= "hassan"
print(bubble_sorting_alphabets(name))