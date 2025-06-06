def sum_digits(s):
    sum = 0
    for char in s:
        if char.isdigit():
            sum += int(char)
    return sum

print(sum_digits("abc12xy3"))