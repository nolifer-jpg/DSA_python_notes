def count_upper_lower(s):
    upper =0
    lower = 0
    for char in s:
        if char.isupper():
            upper +=1
        elif char.islower():
            lower +=1
    return f"Uppercase: {upper}, Lowercase: {lower}"    

print(count_upper_lower("Hello world"))