class Encryption():
    def __init__(self,text,shift):
        self._text = text
        self._shift = shift

    def caesar_cipher(self):
        result = ""
        for char in self._text:
            if char.isupper():
                result += chr(((ord(char)) + self._shift - 65)%26 + 65)

            elif char.islower():
                result += chr(((ord(char)) + self._shift - 97)%26 + 97)
            else:
                result += char

        return result