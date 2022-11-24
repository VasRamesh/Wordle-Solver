# Code to run
import SolverMethods

# Create a list of possible words from the current guesses
possible_words = SolverMethods.read_in_file([])

# Game Loop
for attempts in range(0, 6):
    guess, color = SolverMethods.word_input()
    if color == "ggggg":
        print("Congrats! You Won!")
        break
    temp_removal = []
    for word in possible_words:
        for i in range(5):
            if color[i] == 'y' and guess[i] not in word:
                temp_removal.append(possible_words.index(word))
                break
            elif color[i] == 'b' and guess[i] in word:
                temp_removal.append(possible_words.index(word))
                break
            elif color[i] == 'g' and guess[i] != word[i]:
                temp_removal.append(possible_words.index(word))
                break
            elif color[i] == 'y' and guess[i] is word[i]:
                temp_removal.append(possible_words.index(word))
                break

    # remove by index and update possible_words
    removal = sorted(temp_removal, reverse=True)
    for num in removal:
        del possible_words[num]
    SolverMethods.return_best_guesses(5, possible_words)
