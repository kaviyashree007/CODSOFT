#random is used to select random characters
#string provides a collection of character sets

import random
import string

#It generates a password by randomly selecting characters from this set until the desired length is reached

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

#Prompts the user to enter the desired length of the password and Validates the input to ensure it is a positive integer

def main():
    
    try:
        length = int(input("Enter the length of the password you desire: "))
        if length <= 0:
            raise ValueError("Length you enter should be a positive integer.")
    except ValueError as e:
        print(f"The given input is an Invalid input: {e}")
        return
    
    # Generate the password
    password = generate_password(length)
    
    # Display the password
    print(f"Your Generated password: {password}")

if __name__ == "__main__":
    main()
