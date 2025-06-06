def consecutive_count(s):
    count = 0
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count+=1    
    return count          

print(consecutive_count("aaabbcddaa"))       