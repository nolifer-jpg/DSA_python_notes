def longest_word(sentence):
    words = sentence.split()
    longword = max(words, key=len)
    return longword
