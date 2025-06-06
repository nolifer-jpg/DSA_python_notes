def bubble_sort(lst):
    k=1
    for i in range(len(lst)):
        already_sorted= True
        for j in range(len(lst)-i-1):
            if lst[j]>lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                already_sorted = False
        print(f"Pass {k}: {lst}") 
        k+=1               
        if already_sorted:
            break
    return lst            

bubble_sort([4, 3, 1, 2])