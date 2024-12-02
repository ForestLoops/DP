import itertools

def brute_force_password(target, char_set):
    attempts = 0
    for length in range(1, len(target) + 1):
        for guess in itertools.product(char_set, repeat=length):
            attempts += 1
            guess_password = ''.join(guess)
            if guess_password == target:
                return guess_password, attempts

# Example usage
if __name__ == "__main__":
    target_password = input("Enter the password to crack: ")  # Replace with the target password
    character_set = "abcdefghijklmnopqrstuvwxyz"  # Character set to use in guesses
    
    guessed_password, attempts = brute_force_password(target_password, character_set)
    print(f"Guessed Password: {guessed_password}")
    print(f"Attempts Taken: {attempts}")