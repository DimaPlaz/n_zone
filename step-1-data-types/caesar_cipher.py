"""
Задача реализовать шифр цезаря.
Написать 2 функции.
одна функция принимает строку и ключ, возвращает зашифрованную строку
другя функция принимает зашифрованную строку и ключ, возвращает разшифрованную строку
"""


def encrypt(string, key) -> str:
    ...


def decrypt(string, key) -> str:
    ...


if __name__ == '__main__':
    some_string = 'I am groot'
    some_key = 10

    encrypted_string = encrypt(some_string, key=some_key)
    decrypted_string = decrypt(encrypted_string, key=some_key)

    assert some_string == decrypted_string

