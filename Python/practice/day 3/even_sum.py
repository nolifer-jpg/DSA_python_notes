def even_sum(s):
    sum = 0
    temp_s = list(map(int, s))
    for i in range(1, len(s)+1):
        if i %2 ==0:
            sum += temp_s[i-1]
    return sum

print(even_sum("123456"))        