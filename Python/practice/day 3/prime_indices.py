import math
def prime_indices(s):
    sum =0
  
    for i in range(2, len(s)):
        if prime_checker(i):
            sum += int(s[i])
    return sum  

def prime_checker(n):
    if n <2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i ==0:
            return False
    return True    

print(prime_indices("1234567"))
