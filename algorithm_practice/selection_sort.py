def selection_sort(lst):
    
    for i in range(len(lst)): #moves boundary between sorted and unsorted by 1 each time
        index_of_smallest = i
        
        #find smallest element in the unsorted region
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[index_of_smallest]:
                index_of_smallest = j
        
        if lst[i] != lst[index_of_smallest]: #check for self swap
            #swap current with the newfound smallest
            lst[i], lst[index_of_smallest] = lst[index_of_smallest], lst[i]
    
    return lst

lst = [3, 2, 1, 5, 7, 1, 2]
print(selection_sort(lst))
