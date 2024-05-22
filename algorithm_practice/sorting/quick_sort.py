def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    
    pivot = lst[len(lst) // 2] #midpoint
    left = [x for x in lst if x < pivot]
    middle = [x for x in lst if x == pivot]
    right = [x for x in lst if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

def quick_sort_inplace(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort_inplace(arr, low, pivot - 1)  
        quick_sort_inplace(arr, pivot + 1, high)

def partition(arr, low, high):
    pivot = arr[high] 
    i = low - 1 
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i] 
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1 #return partitioning index

lst = [3, 2, 1, 5, 7, 1, 2]
quick_sort_inplace(lst, 0, 6)
print(lst)
