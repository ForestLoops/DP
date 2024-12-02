import hashlib

# Function to hash a password using SHA-256
def hash_password(password):
    sha256_hash = hashlib.sha256(password.encode())
    return sha256_hash.hexdigest()

# Get password input from the user
password = input("Enter the password: ")

# Print the SHA-256 hashed password
hashed_password = hash_password(password)
print("SHA-256 hashed password:", hashed_password)
