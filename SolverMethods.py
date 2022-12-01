# Methods for SolverCode

# Method to read in the file:
def read_in_file(list_of_words: list):
    try:
        words_file = open("wordle-nyt-answers-alphabetical.txt", "r")
        for word in words_file:
            list_of_words.append(word)
        words_file.close()
    except FileNotFoundError:
        print("File Not Found")
    return list_of_words


# Method that asks for information:
def word_input():
    word: str = input("What was your guess (LOWERCASE): ")
    # word_char_list = []
    if len(word) > 5:
        raise Exception("Guess is too long")

    color: str = input("Color attributes: (LOWERCASE, g, y, b): ")
    # color_int_list = []
    if len(color) > 5:
        raise Exception("Guess is too long")
    return word, color


# Print next best guesses
def return_best_guesses(n, list):
    print("Best guesses: ")
    if n > len(list):
        n = len(list)
    if len(list) == 0:
        print("Error: Word Not found")
    for i in range(n):
        print(list[i])
