def insertion_sort(lst):
    
    for i in range(1, len(lst)): #for each element in unsorted
        
        #iterate backwards through sorted to find the right place
        for j in range(i - 1, -1, -1):
            if lst[i] > lst[j]: #if right place, stop
                break
            else: #swap
                lst[i], lst[j] = lst[j], lst[i]
                i = j
                
    return lst

lst = [8, 9, 2, 10, 27, 1, -80]
print(insertion_sort(lst))
