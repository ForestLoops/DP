
# Function to encrypt the message using Rail Fence Cipher
def encrypt_rail_fence(text, key):
    rail = [['\n' for i in range(len(text))] for j in range(key)]
    
    direction_down = False
    row, col = 0, 0
    
    for char in text:
        if row == 0 or row == key - 1:
            direction_down = not direction_down
        rail[row][col] = char
        col += 1
        row += 1 if direction_down else -1
    
    result = []
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])
    return "".join(result)

# Function to decrypt the message using Rail Fence Cipher
def decrypt_rail_fence(cipher, key):
    rail = [['\n' for i in range(len(cipher))] for j in range(key)]
    
    direction_down = None
    row, col = 0, 0
    
    for i in range(len(cipher)):
        if row == 0:
            direction_down = True
        if row == key - 1:
            direction_down = False
        rail[row][col] = '*'
        col += 1
        row += 1 if direction_down else -1

    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if rail[i][j] == '*' and index < len(cipher):
                rail[i][j] = cipher[index]
                index += 1

    result = []
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
            direction_down = True
        if row == key - 1:
            direction_down = False
        if rail[row][col] != '\n':
            result.append(rail[row][col])
            col += 1
        row += 1 if direction_down else -1
    return "".join(result)

# Get input from the user
text = input("Enter the message: ")
key = int(input("Enter the number of rails: "))

# Perform encryption
encrypted_text = encrypt_rail_fence(text, key)
print("Encrypted message:", encrypted_text)

# Perform decryption
decrypted_text = decrypt_rail_fence(encrypted_text, key)
print("Decrypted message:", decrypted_text)
