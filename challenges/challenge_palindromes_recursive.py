def is_palindrome_recursive(word, low_index, high_index):
    if not isinstance(word, str) or len(word) == 0:
        return False
    if word[low_index] != word[high_index]:
        return False
    if high_index <= low_index:
        return True
    if high_index + 1 > low_index:
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)
    return True
