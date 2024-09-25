# sorting in ascending order
def selection_sorting(array):
    n=len(array)
    for i in range(n-1):
        least = i
        for j in range(i+1 ,n ):
            if array[j] < array[least]:
                least = j
        array[i] , array[least] = array[least] , array[i]
    return array

arr = [15 , 30 , 10 , 8 , 20 , 1]
print(selection_sorting(arr))


#sorting in descending_order

def selection_sorting(array):
    n = len(array)
    for i in range(n-1):
        highest=i
        for j in range(i+1 , n):
            if array[j] > array[highest]:
                highest = j
        array[i] , array[highest] = array[highest] , array[i]
    return array

arr = [15 , 30 , 10 , 8 , 20 , 1]
print(selection_sorting(arr))










        
                

