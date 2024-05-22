def shell_sort(lst):
    gaps = generate_sequence(lst)
    
    for gap in gaps:
        #run insertion sort on the elements that are gap apart
        for i in range(1, len(lst), gap):
        
            #iterate backwards through sorted to find the right place
            for j in range(i - 1, -1, -1):
                if lst[i] > lst[j]: #if right place, stop
                    break
                else: #swap
                    lst[i], lst[j] = lst[j], lst[i]
                    i = j
    return lst
    
def generate_sequence(lst):
    res = []
    i = 1
    while i < (len(lst) / 2):
        res.append(i)
        i *= 2
    res.reverse()
    return res


lst = [87, 3, 90, 100, 4, 7, 2]
print(shell_sort(lst))
