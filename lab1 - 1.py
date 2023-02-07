list = ["apple", "chestnut", "gargoyle", "pandas", "sheep", "raptor"]

longest_word = 0
longest_word_in_list = ""

for i in range(len(list)):
  if len(list[i]) > longest_word:
    longest_word = len(list[i])
    longest_word_in_list = list[i]
    
print(longest_word_in_list)
  
 
  
  