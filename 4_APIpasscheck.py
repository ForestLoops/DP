import hashlib
import requests

HIBP_API_KEY = 'your_api_key_here'
HIBP_API_URL = "https://api.pwnedpasswords.com/range/"

# Function to check if a password has been leaked
def check_password_leak(password):
    # Hash the password using SHA-1
    sha1_password = hashlib.sha1(password.encode()).hexdigest().upper()
    prefix = sha1_password[:5]
    suffix = sha1_password[5:]

    # Send a request to the HIBP API
    headers = {"hibp-api-key": HIBP_API_KEY}
    response = requests.get(HIBP_API_URL + prefix, headers=headers)
    
    if response.status_code != 200:
        raise Exception(f"Error querying HIBP API: {response.status_code}")
    
    hashes = response.text.splitlines()
    for line in hashes:
        hash_suffix, count = line.split(":")
        if hash_suffix == suffix:
            return int(count)
    return 0

# Function to process the file
def check_passwords_in_file(file_path):
    with open(file_path, "r") as file:
        for line in file:
            username, password = line.strip().split(",")
            leak_count = check_password_leak(password)
            if leak_count > 0:
                print(f"Warning: Password for {username} has been leaked {leak_count} times!")
            else:
                print(f"Password for {username} is safe (not found in data breaches).")
# Get file path from the user
file_path = input("Enter the path to the file containing usernames and passwords: ")
check_passwords_in_file(file_path)



