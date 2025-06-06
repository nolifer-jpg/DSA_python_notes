def even_sq_sum(s):
    sum =0
    for char in s:
        digit = int(char)
        if digit %2==0:
            sum += digit**2
    return sum

print(even_sq_sum("123456"))