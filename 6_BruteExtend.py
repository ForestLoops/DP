import itertools
import time

def brute_force_password(target, char_set, max_length):
    attempts = 0
    start_time = time.time()
    
    for length in range(1, max_length + 1):
        for guess in itertools.product(char_set, repeat=length):
            attempts += 1
            guess_password = ''.join(guess)
            if guess_password == target:
                end_time = time.time()
                return guess_password, attempts, end_time - start_time
    
    end_time = time.time()
    return None, attempts, end_time - start_time

# Example usage
if __name__ == "__main__":
    target_password = input("Enter the password to crack: ")
    max_length = int(input("Enter the maximum length to attempt: "))
    
    # Predefined character set: includes lowercase, uppercase, digits, and special characters
    character_set = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    
    print("Starting brute-force attack...")
    guessed_password, attempts, time_taken = brute_force_password(target_password, character_set, max_length)
    
    if guessed_password:
        print(f"Guessed Password: {guessed_password}")
        print(f"Attempts Taken: {attempts}")
        print(f"Time Taken: {time_taken:.2f} seconds")
    else:
        print("Failed to crack the password within the given length and character set.")
        print(f"Attempts Taken: {attempts}")
        print(f"Time Taken: {time_taken:.2f} seconds")
