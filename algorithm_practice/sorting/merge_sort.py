def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    
    midpoint = len(lst) // 2
    left = merge_sort(lst[:midpoint])
    right = merge_sort(lst[midpoint:])
    return merge(left, right)

#joins 2 lists into 1 sorted list
def merge(l1, l2):
    p1, p2 = 0, 0
    res = []
    
    while p1 < len(l1) and p2 < len(l2):
        if l1[p1] < l2[p2]:
            res.append(l1[p1])
            p1 += 1
        else:
            res.append(l2[p2])
            p2 += 1
            
    if p1 == len(l1): #went through all of l1
        res += l2[p2:]
    else:
        res += l1[p1:]
        
    return res

lst = [3, 2, 1, 5, 7, 1, 2]
print(merge_sort(lst))
