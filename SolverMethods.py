# Methods for SolverCode

# Method that updates the current_words list based on provided information:
def update_list(list_letters: list, list_colors: list, current_words: list):

    # Exceptions
    if len(list_letters) > 5 or len(list_colors) > 5:
        raise Exception("Input list size greater than 5")
    for i in range(5):
        if list_colors[i] > 2 or list_colors[i] < 0:
            raise Exception("Invalid inputs for list_colors")

    # eliminate words
    for i in range(5):
        # Grey Case: Letter is not in word
        if list_colors[i] is 0:
            for word in current_words:
                if word[i] is list_letters[i]:
                    current_words.remove(word)
        # Green Case: Letter is in correct position and guess
        if list_colors[i] is 2:
            for word in current_words:
                if word[i] is not list_letters[i]:
                    current_words.remove(word)
        # Special Yellow case
        if list_colors[i] is 1:  # yellow: letter is in the wrong place
            for word in current_words:
                bool_for_word = False
                for j in range(5):
                    if word[j] is list_letters[j]:
                        current_words.remove(word)
                        break
                    if word[j] is list_letters[i]:
                        bool_for_word = True
                if bool_for_word is False:
                    current_words.remove(word)
    return


# Method to read in the file:
def read_in_file(list_of_words: list):
    words_file = open("words.txt", "r")
    for word in words_file:
        list_of_words.append(word)
    words_file.close()

# Method that asks for information:
def word_input():
    word: str = input("What was your guess (LOWERCASE): ")
    word_char_list = []
    if len(word) > 5:
        raise Exception("Guess is too long")

    # Put guess into list
    for i in range(5):
        word_char_list[i] = word[i]

    color: str = input("What was your guess (LOWERCASE): ")
    color_int_list = []
    if len(color) > 5:
        raise Exception("Guess is too long")

    # Put guess into list
    for i in range(5):
        color_int_list[i] = color[i]

    return word_char_list, color_int_list
