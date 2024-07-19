# shifting
# chr adalah angka ke huruf
def debugging(text):
    debugging = ord(text)
    print(debugging)
    print(chr(debugging))

def caesar_cipher(text,shift):
    result = ""
    for char in text:
        # isuppper --> uppercase
        if char.isupper():
            debugging(char)
            result += chr(((ord(char)) + shift - 65)%26 + 65)

        elif char.islower():
            debugging(char)
            result += chr(((ord(char)) + shift - 97)%26 + 97)
        else:
            result += char

    return result

text = "Hello world"
shift = 3
encrypted = caesar_cipher(text,shift)
print("encrypted: " , encrypted)

decripted = caesar_cipher(encrypted,-shift)
print("decripted: ", decripted)