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


# Count word frequency
def word_frequency(paragraph):
    paragraph = str(paragraph)
    counts = dict()
    word_list = paragraph.split()
    for word in word_list:
        counts[word] = counts.get(word, 0) + 1
    return counts


# Find the common word
def common_word(counts):
    big_count = None
    big_word = None
    counts = dict(counts)
    for word, count in counts.items():
        if big_count is None or count > big_count:
            big_word = word
            big_count = count
    print(big_word, big_count)


def main():
    word = str("programming")
    print(letter_frequency(word))
    paragraph = "programming Kevin Kevin"
    print(word_frequency(paragraph))
    common_word(word_frequency(paragraph))


main()
