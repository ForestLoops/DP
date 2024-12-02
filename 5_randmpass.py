import random

def generate_password(num_words):
    with open(r'C:\Users\rahul\Desktop\VS_Code\Github\dict.txt', 'r') as file:
        words = file.read().splitlines()
    
    password = ''.join(random.choices(words, k=num_words))
    return password

# Example usage
num_words = 4
password = generate_password(num_words)
print(f"Generated password: {password}")
