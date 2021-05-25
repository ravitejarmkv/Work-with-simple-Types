def reverse(word):
    # Character count
    char_count = len(word)

    i = char_count
    result = ""
    while i > 0:
        i = i - 1
        result = result + word[i]
    return result


stringReverse = reverse("string")

print(stringReverse)

