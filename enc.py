encryption_key = {
    'a': 'm', 'b': 'n', 'c': 'o', 'd': 'p', 'e': 'q', 'f': 'r', 'g': 's', 'h': 't',
    'i': 'u', 'j': 'v', 'k': 'w', 'l': 'x', 'm': 'a', 'n': 'b', 'o': 'c', 'p': 'd',
    'q': 'e', 'r': 'f', 's': 'g', 't': 'h', 'u': 'i', 'v': 'j', 'w': 'k', 'x': 'l',
    'y': 'z', 'z': 'y', ' ': ' '
}

encrypted = ""

def encrypt(text):
    global encrypted
    l = list(text)
    for i in l:
        if i in encryption_key:
            encrypted += encryption_key[i]
        else:
            encrypted += i

text=input("Enter Text you want to encrypt : ")
encrypt(text)
print(encrypted)
input()