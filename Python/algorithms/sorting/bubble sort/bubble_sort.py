def main():
    lst = [6, 2, 5, 4]
    print(bubble_sort(lst))

def bubble_sort(l):
    for i in range(len(l)):
        already_sorted = True
        for j in range(len(l)-i-1):
            if l[j]>l[j+1]:
                l[j], l[j+1]= l[j+1], l[j]
                already_sorted= False
        if already_sorted:
            break        
    return l

main()
