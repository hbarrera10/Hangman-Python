import random


def play_hangman():
  # Create a list of words

  with open("words.txt") as f:
    words = f.read().split("\n")

  # Pick a random word
  word = random.choice(words)

  # Create a list of underscores that represents the letters in the word
  underscores = ["_"] * len(word)

  # Set the number of incorrect guesses to 0
  incorrect_guesses = 0

  # Set a maximum number of incorrect guesses
  max_incorrect_guesses = 6

  # Set a flag to check if the game is over
  game_over = False

  while not game_over:
    # Print the current state of the game
    print("Word: ", " ".join(underscores))
    print("Incorrect guesses: ", incorrect_guesses)

    # Prompt the user for a letter
    letter = input("Enter a letter or word: ")

    #checks length of input
    if len(letter) == len(word):
      if letter == word:
        for index in range(len(underscores)):
          underscores[index] = word[index]
        game_over = True
      else:
        incorrect_guesses += 1


    # Check if the letter is in the word
    elif letter in word:
      # If the letter is in the word, replace the underscore at the correct index with the letter
      for i in range(len(word)):
        if word[i] == letter:
          underscores[i] = letter
    else:
      # If the letter is not in the word, increment the number of incorrect guesses
      incorrect_guesses += 1

    # Check if the game is over
    if incorrect_guesses >= max_incorrect_guesses:
      game_over = True
      print("You lose! The word was: ", word)
    elif "_" not in underscores:
      game_over = True
      print("You win! The word was: ", word)

# Start the game
play_hangman()
