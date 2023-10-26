def Ency():  
    encryption_key = {
        'a': 'm', 'b': 'n', 'c': 'o', 'd': 'p', 'e': 'q', 'f': 'r', 'g': 's', 'h': 't',
        'i': 'u', 'j': 'v', 'k': 'w', 'l': 'x', 'm': 'a', 'n': 'b', 'o': 'c', 'p': 'd',
        'q': 'e', 'r': 'f', 's': 'g', 't': 'h', 'u': 'i', 'v': 'j', 'w': 'k', 'x': 'l',
        'y': 'z', 'z': 'y', ' ': ' '
    }

    encrypted = ""

    def encrypt(text):
        result = ""  # Use a local variable
        l = list(text)
        for i in l:
            if i in encryption_key:
                result += encryption_key[i]
            else:
                result += i
        return result

    text = input("Enter Text you want to encrypt: ")
    encrypted = encrypt(text)
    print(encrypted)

def Decry():
    decryption_key = {
        'm': 'a', 'n': 'b', 'o': 'c', 'p': 'd', 'q': 'e', 'r': 'f', 's': 'g', 't': 'h',
        'u': 'i', 'v': 'j', 'w': 'k', 'x': 'l', 'a': 'm', 'b': 'n', 'c': 'o', 'd': 'p',
        'e': 'q', 'f': 'r', 'g': 's', 'h': 't', 'i': 'u', 'j': 'v', 'k': 'w', 'l': 'x',
        'z': 'y', 'y': 'z', ' ': ' '
    }

    decrypted = ""

    def decrypt(text):
        result = ""  # Use a local variable
        l = list(text)
        for i in l:
            if i in decryption_key:
                result += decryption_key[i]
            else:
                result += i
        return result

    text = input("Enter Text you want to decrypt: ")
    decrypted = decrypt(text)
    print(decrypted)

print(" 1. press '1' for Encrypt a text ")
print(" 2. press '2' for Decrypt a text  Encrypted Text")
user = int(input("Enter your choice: "))
if user == 1:
    Ency()
elif user == 2:
    Decry()
else:
    print("Invalid choice")
