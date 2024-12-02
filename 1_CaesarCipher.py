# Caesar Cipher Encryption and Decryption 
def encrypt(text, shift): 
    encrypted_text = "" 
    for char in text: 
        if char.isupper(): 
            encrypted_text += chr((ord(char) + shift - 65) % 26 + 65) 
        elif char.islower(): 
            encrypted_text += chr((ord(char) + shift - 97) % 26 + 97) 
        else: 
            encrypted_text += char 
    return encrypted_text
 
def decrypt(text, shift): 
    decrypted_text = "" 
    for char in text: 
        if char.isupper(): 
            decrypted_text += chr((ord(char) - shift - 65) % 26 + 65) 
        elif char.islower(): 
            decrypted_text += chr((ord(char) - shift - 97) % 26 + 97) 
        else: 
           decrypted_text += char 
    return decrypted_text
 
text = input("Enter the text to encrypt: ") 
shift = int(input("Enter the shift value: ")) 
encrypted_text = encrypt(text, shift) 
decrypted_text = decrypt(encrypted_text, shift) 
print("Encrypted Text: ", encrypted_text) 
print("Decrypted Text: ", decrypted_text)