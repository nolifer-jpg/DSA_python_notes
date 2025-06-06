def selection_sort(lst):
    swaps = 0
    comparisions =0
    k=1
    for i in range(0, len(lst)-1):
        min_value = i
        for j in range(i+1, len(lst)):
            comparisions +=1 
            if lst[j]<lst[min_value]:
                min_value = j 
        if min_value != i:
            lst[min_value], lst[i] = lst[i], lst[min_value]
            swaps+=1
        print(f"Pass {k}: {lst}")  
        k+=1
    return f"Total Swaps: {swaps}\nTotal Comparisions: {comparisions}"

print(selection_sort([6, 3, 4, 2]))