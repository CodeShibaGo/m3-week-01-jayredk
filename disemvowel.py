def disemvowel(s):
    string = ''
    vowel = ['a', 'e', 'i', 'o', 'u']
    for char in s:
        if char.lower() in vowel:
            continue
        string += char

    return string
