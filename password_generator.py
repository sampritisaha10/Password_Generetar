import random
import string

print("==== PASSWORD GENERATOR ====")

# Take password length from user
length = int(input("Enter password length: "))

# Ask user preferences
include_uppercase = input("Include uppercase letters? (yes/no): ").lower()
include_numbers = input("Include numbers? (yes/no): ").lower()
include_symbols = input("Include symbols? (yes/no): ").lower()

# Base characters
characters = string.ascii_lowercase

# Add uppercase letters
if include_uppercase == "yes":
    characters += string.ascii_uppercase

# Add numbers
if include_numbers == "yes":
    characters += string.digits

# Add symbols
if include_symbols == "yes":
    characters += string.punctuation

# Generate password
password = ""

for i in range(length):
    password += random.choice(characters)

# Display password
print("\nGenerated Password:", password)