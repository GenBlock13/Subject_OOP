def ceaser(text, shift):
    code_text = ''
    for char in text:
        if char.isalpha() and char.islower():
            ascii_code = ord(char)
            encrypted_code = (ascii_code - 97 + shift) % 26 + 97
            code_text += chr(encrypted_code)

        elif char.isalpha() and char.isupper():
            ascii_code = ord(char)
            encrypted_code = (ascii_code - 65 + shift) % 26 + 65
            code_text += chr(encrypted_code)
        else:
            code_text += char
    return code_text


def ceaser_ans(text, shift):
    code_text = ''
    for char in text:
        if char.isalpha() and char.islower():
            ascii_code = ord(char)
            encrypted_code = (ascii_code - 97 - shift) % 26 + 97
            code_text += chr(encrypted_code)

        elif char.isalpha() and char.isupper():
            ascii_code = ord(char)
            encrypted_code = (ascii_code - 65 - shift) % 26 + 65
            code_text += chr(encrypted_code)

        else:
            code_text += char
    return code_text
