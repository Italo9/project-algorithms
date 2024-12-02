def is_palindrome_iterative(word):
    if not isinstance(word, str) or len(word) == 0:
        return False
    # invertendo sequência usando notação: (referencia bibliografica abaixo)
    #  https://forum.freecodecamp.org/t/how-to-use-python-slice-with-the-start-stop-and-step-arguments-explained-with-examples/19202
    if word == word[::-1]:
        return True
    if word != word[::-1]:
        return False
