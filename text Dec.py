decryption_key = {
    'm': 'a', 'n': 'b', 'o': 'c', 'p': 'd', 'q': 'e', 'r': 'f', 's': 'g', 't': 'h',
    'u': 'i', 'v': 'j', 'w': 'k', 'x': 'l', 'a': 'm', 'b': 'n', 'c': 'o', 'd': 'p',
    'e': 'q', 'f': 'r', 'g': 's', 'h': 't', 'i': 'u', 'j': 'v', 'k': 'w', 'l': 'x',
    'z': 'y', 'y': 'z', ' ': ' '
}

decrypted = ""

def decrypt(text):
    global decrypted
    l = list(text)
    for i in l:
        if i in decryption_key:
            decrypted += decryption_key[i]
        else:
            decrypted += i

text = input("Enter Text you want to decrypt: ")
decrypt(text)
print(decrypted)
