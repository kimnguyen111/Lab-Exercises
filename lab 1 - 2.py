import random
sowpods = "sowpods.txt"

def longest_word(list):
  longest_word = 0
  longest_word_in_list = ""
  for i in range(len(list)):
    if len(list[i]) > longest_word:
      longest_word = len(list[i])
      longest_word_in_list = list[i]
  return longest_word_in_list
    
def word_generator():
  filename = sowpods
  f = open(filename, "r", encoding="utf8")
  words = f.readlines()
  f.close()
  return random.choice(words).strip()

def main():
  list = ["apple", "chestnut", "gargoyle", "pandas", "sheep", "raptor"]
  for i in range (7):
    list.append(word_generator())
  print(list)
  print(longest_word(list))
    
main()


