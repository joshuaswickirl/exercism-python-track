def is_isogram(string):
    chars_used = set()

    for char in string.lower():
        if char in chars_used:
            return False
        else:
            if char.isalpha():
                chars_used.add(char)

    return True
