#!/usr/bin/env python3
# Created by Maximiliano Fairman
# Created on Nov 5th, 2025
# This program that asks the user to provide.
# A single character from the alphabet
# and then prints "Vowel" or "Consonant"
# depending on the letter entered.
def main():

    # blank line for readability
    print(" ")
    # Greating to the user on start
    print("Welcome! This program will tell you")
    print("if the letter you enter")
    print("is either a Vowel or a Consonant.")
    # blank line for readability
    print(" ")

    # Ask user to input a letter
    letter = input("Enter a single letter from the alphabet: ")

    # Check if input has exactly one character (without using len)
    try:
        # checks if its one character
        # (non taught)
        first_char = letter[0]
        # checks if theres two or more characters
        # (non taught)
        extra_char = letter[1]

        # if there is more than one character
        print("Please enter ONE letter.")
        return

    # If there is one character
    except IndexError:
        letter = first_char

    # Check if it's a valid letter
    if not letter.isalpha():
        # (non taught)
        print("Please enter only letters.")
        return

    # If the letter is Y or y
    if letter == ["y", "Y"]:
        print(f"{letter} is both a Vowel and a Consonant.")
        return

    # Check if the letter is a vowel
    if letter in ["a", "e", "i", "o", "u"] or letter in ["A", "E", "I", "O", "U"]:
        print(f"{letter} is a Vowel.")
    # if instead the letter is a consonant
    else:
        print(f"{letter} is a Consonant.")


if __name__ == "__main__":
    main()
