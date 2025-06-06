def product_even_index(s):
    product = 1
    for i in range(0, len(s), 2):
        product *= int(s[i])
    return product


print(product_even_index("123456"))