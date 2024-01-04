def find_capitals(word):
    str = ''
    
    for char in word:
        c = ord(char)
        if c < 97 and c >= 65:
            str += char
    return str