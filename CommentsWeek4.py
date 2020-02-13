# Why comments
# Readability
# Describe what is going on in a sequence of code
# Document who wrote the code
# Turn off a line of code


# Open a file
def open_file():
    file_name = input("Enter file: ")
    paragraph = open(file_name, 'r')


# Count letter frequency
def letter_frequency(word):
    counts = dict()
    for letter in word:
        counts[letter] = counts.get(letter, 0) + 1
    return counts


def main():
    word = str("programming")
    print(letter_frequency(word))


main()
