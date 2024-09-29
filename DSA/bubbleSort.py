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