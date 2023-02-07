#generate word
word = "boteu"
chances = 8
occupiedSpaces = 0

#game directions
print(
  "Welcome to Hangman! Please take a piece of paper to keep track of the game. The word has",
  len(word), "letters so draw", len(word), "spaces.")
print()
print(
  "The spaces correspond to numbers. Number 0 will be the very left spot and Number 4 will be the very spot. Please write these numbers under your spaces."
)
print()

#game on
while chances > 0:
  guess = input("Guess a letter: ")
  inWord = False
  for i in range(len(word)):
    if guess == word[i]:
      occupiedSpaces = occupiedSpaces + 1
      print("You're correct!", guess, "is in the Number", i, "spot")
      inWord = True
  if inWord == False:
    chances = chances - 1
    print("Oh man.. you're wrong. You still have", chances, "chances left")
  if occupiedSpaces == len(word):
    print("HORRAY! YOU WIN!")
    break
  if chances == 0:
    print("You lost. You will never know the word...")
