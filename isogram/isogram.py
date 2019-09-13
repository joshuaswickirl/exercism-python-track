def is_isogram(string):
    chars_used = set()
    is_isogram = True

    for char in string.lower():
        if char in chars_used:
            is_isogram = False
            break
        else:
            if char not in [' ','-']:
                chars_used.add(char)

    return is_isogram
