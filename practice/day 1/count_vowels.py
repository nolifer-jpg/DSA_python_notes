def count_vowels(s):
    s = s.lower()
    vowels = "aeiou"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count        
