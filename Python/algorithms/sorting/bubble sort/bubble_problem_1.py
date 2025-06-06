def main():
    lst = [6, 2, 5, 4]
    print(bubble_sort(lst))



def bubble_sort(lst):
    swaps =0 
    comparisions =0
    for i in range(len(lst)):
        already_sorted = True
        for j in range(len(lst)-i-1):
            if lst[j]>lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                print(lst)
                swaps +=1
                already_sorted = False
            comparisions+=1    
        if already_sorted:
            break
    return f"{lst}, Swaps: {swaps}, Comparisions: {comparisions}"
main()