def count_digits(s):
    count =0
    for char in s:
        if char.isdigit():
            count+=1
    return count

print("Total Digits:", count_digits("abc123xyz9"))  