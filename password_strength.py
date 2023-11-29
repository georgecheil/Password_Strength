import re
import math
import termcolor

def is_strong_password(password):
    # Check length
    if len(password) < 8:
        return False

    # Check for uppercase, lowercase, and numbers
    if not re.search(r"[A-Z]", password) or \
       not re.search(r"[a-z]", password) or \
       not re.search(r"\d", password):
        return False

    # Check for special characters
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False

    return True

def calculate_entropy(password):
    # Define character sets and their sizes
    uppercase_letters = 26
    lowercase_letters = 26
    digits = 10
    special_characters = 22  

    # Calculate entropy in bits
    character_set_size = uppercase_letters + lowercase_letters + digits + special_characters
    entropy = len(password) * math.log2(character_set_size)

    return entropy

def time_to_crack(entropy, guesses_per_second):
    guesses = 2 ** entropy
    time_seconds = guesses / guesses_per_second
    return time_seconds

# Get the password from the user
password = input("Enter a password: ")

# Calculate and print password entropy
entropy = calculate_entropy(password)
print(f"Password entropy: {entropy:.2f} bits")

# Estimate time to crack (assuming 10^12 guesses per second)
guesses_per_second = 1e12
time_seconds = time_to_crack(entropy, guesses_per_second)

# Convert seconds to a more human-readable format
minutes, seconds = divmod(time_seconds, 60)
hours, minutes = divmod(minutes, 60)
days, hours = divmod(hours, 24)

print(f"Estimated time to crack: {int(days)} days, {int(hours)} hours, {int(minutes)} minutes, {int(seconds)} seconds")



# Check the strength of the password
if is_strong_password(password):
    print(termcolor.colored("Strong password!", 'green'))
else:
    print(termcolor.colored("Weak password. Please make sure it has at least 8 characters, including uppercase, lowercase, numbers, and special characters.", 'red'))
