# Simple program to list each word in a text that is entered by the user
# and to count the number of time each word is used in the entered text.

# variable to hold users inputed text
sentence= input("Type your text here to count the words: ")


# function to perform described task
def counting_wordfunc(sentence):
  # variable and dictionary used in the function
  new_sentence= sentence.split()
  counting_words= {}
  
  
  # the part of the function that adds words to the dictionary and counts
  # each time the word is used
  for word in new_sentence:
    if word not in counting_words:
      counting_words[word] = 1
    else:
      counting_words[word] += 1
  # returns the value of the completed dictionary  
  return counting_words
  
# prints a line to tell the user what is to folow  
print("Here is a count of each word in the text you entered:") 

# prints the result of the function
print(counting_wordfunc(sentence))

  
