# Programmers: Liv Oakes
# Course:  CS151, Dr. Zee
# Due Date: 21 November 2024
# Lab Assignment: PA4
# Problem Statement:This program analyzes news headlines from the Australian Broadcasting Company (ABC).
#                    It allows users to perform various analyses, such as counting headlines containing a specific word,
#                    writing those headlines to a new file, calculating the average number of characters per headline,
#                   and identifying the longest and shortest headlines.
# Data In: 1. The name of the file containing the headlines to analyze.
#          2. User's choice of analysis to perform (options 1-6).
#          3. A specific word to search for in the headlines (for options 1 and 2).
#          4. The name of the output file (for option 2).
#          5. A new file name to read (for option 5).
# Data Out:  1. The name of the file containing the headlines to analyze.
#            2. The number of headlines containing a specific word.
#            3. A confirmation that headlines containing a specific word have been written to an output file.
#            4. The average number of characters per headline.
#            5. The longest and shortest headlines along with their character counts.
#            6. A goodbye message when the user chooses to quit the program.
# Credits: This code is based on concepts and examples discussed in our lectures.
# Input Files: Events from 2014, 2015, 2016, 2017, 2018, and 2019


import os

# Purpose: Reads a file and returns a list of lines stripped of whitespace.
# Parameters: filename
# Return: A list of strings that each represent a line from the file.
def read_file(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file]

# Purpose: Counts the number of headlines that contain a specific word.
# Parameters: headlines
# Return: The count of headlines containing the specified word.
def count_word(headlines, word):
    return sum(1 for headline in headlines if word.lower() in headline.lower())

# Purpose:  Writes headlines that contain a specific word to a new file.
# Parameters: headlines, word, output_file
# Return: None
def write_headlines_with_word(headlines, word, output_file):
    with open(output_file, 'w') as file:
        for headline in headlines:
            if word.lower() in headline.lower():
                file.write(headline + '\n')

# Purpose: Calculates the average number of characters per headline.
# Parameters: headlines
# Return: The average number of characters per headline.
def average_characters(headlines):
    return sum(len(headline) for headline in headlines) / len(headlines)

# Purpose: Finds the longest and shortest headlines.
# Parameters: headlines
# Return: The longest headline and the shortest headline.
def longest_shortest_headline(headlines):
    longest = max(headlines, key=len)
    shortest = min(headlines, key=len)
    return longest, shortest

# Purpose: Main function to run the ABC News Headlines Analyzer. This function handles user interaction and calls other functions
        #to perform various analyses on the headlines.
# Parameters: None
# Return: None
def main():
    print("Welcome to the ABC News Headlines Analyzer!")
    print("This program allows you to analyze headlines from the Australian Broadcasting Company.")
    print("--------------------------------------")

    headlines = []
    filename = input("Enter the name of the file to analyze (e.g., 2014.txt): ")

    while not os.path.exists(filename):
        print("File not found. Please try again.")
        filename = input("Enter the name of the file to analyze (e.g., 2014.txt): ")

    headlines = read_file(filename)
    print(f"File '{filename}' loaded successfully.")

    continue_program = True
    while continue_program:
        print("\nWhat would you like to do?")
        print("1. Count headlines with a specific word")
        print("2. Write headlines with a specific word to a new file")
        print("3. Calculate average characters per headline")
        print("4. Find longest and shortest headlines")
        print("5. Read a new file")
        print("6. Quit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            word = input("Enter the word to search for: ")
            count = count_word(headlines, word)
            print(f"Number of headlines containing '{word}': {count}")

        elif choice == '2':
            word = input("Enter the word to search for: ")
            output_file = input("Enter the name of the output file: ")
            write_headlines_with_word(headlines, word, output_file)
            print(f"Headlines containing '{word}' have been written to '{output_file}'.")

        elif choice == '3':
            avg = average_characters(headlines)
            print(f"Average number of characters per headline: {avg:.2f}")

        elif choice == '4':
            longest, shortest = longest_shortest_headline(headlines)
            print(f"Longest headline ({len(longest)} characters): {longest}")
            print(f"Shortest headline ({len(shortest)} characters): {shortest}")

        elif choice == '5':
            filename = input("Enter the name of the new file to analyze: ")
            if os.path.exists(filename):
                headlines = read_file(filename)
                print(f"File '{filename}' loaded successfully.")
            else:
                print("File not found. Please try again.")

        elif choice == '6':
            print("Thank you for using the ABC News Headlines Analyzer. Goodbye!")
            continue_program = False

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
main()