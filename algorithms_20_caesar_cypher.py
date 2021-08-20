# Dobre wzorce:

# from string import ascii_lowercase, ascii_uppercase
# abc = list(ascii_lowercase)
# ABC = list(ascii_uppercase)

# def caesar_cypher_encrypt(s, key):
#     return ''.join(map(lambda x: abc[(abc.index(x)+key)%len(abc)] if x in abc else (ABC[(ABC.index(x)+key)%len(ABC)] if x in ABC else x), s))

# def caesar_cypher_decrypt(s, key):
#     return ''.join(map(lambda x:abc[(abc.index(x)-key)%len(abc)] if x in abc else (ABC[(ABC.index(x)-key)%len(ABC)] if x in ABC else x), s))
###################################



from string import ascii_lowercase, ascii_uppercase

def caesar_cypher_encrypt(s, key):
    encrypted = ""

    def encrypt(char, key, dict=ascii_lowercase):
        index = dict.index(char)
        new_index = int(index) + key
        if new_index > 25:
            new_index -= 26
        return dict[new_index]

    for i in s:        
        if i in ascii_lowercase:
            encrypted += encrypt(i, key, ascii_lowercase)            
        elif i in ascii_uppercase:
            encrypted += encrypt(i, key, ascii_uppercase)
        else:
            encrypted += i
    return encrypted

def caesar_cypher_decrypt(s, key):
    decrypted = ""

    def decrypt(char, key, dict=ascii_lowercase):
        index = dict.index(char)
        new_index = int(index) - key
        if new_index < 0:
            new_index += 26
        return dict[new_index]

    for i in s:        
        if i in ascii_lowercase:
            decrypted += decrypt(i, key, ascii_lowercase)            
        elif i in ascii_uppercase:
            decrypted += decrypt(i, key, ascii_uppercase)
        else:
            decrypted += i
    return decrypted



# def caesar_cypher_decrypt(s, key):
#     ...


if __name__ == "__main__":
    

    # print(caesar_cypher_decrypt("Qzuipo jt tvqfs ejtdp !", 1))

    print(caesar_cypher_encrypt("Python is super disco !", 1))
    print(
        caesar_cypher_decrypt(caesar_cypher_encrypt("Python is super disco !", 11), 11)
    )