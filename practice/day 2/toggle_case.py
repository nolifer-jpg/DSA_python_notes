def toggle_case(s):
    result = ""
    for char in s:
        if char.islower():
            result += char.upper()
        else:
            result += char.lower()
    return result

print(toggle_case("HelloWorld"))                     
