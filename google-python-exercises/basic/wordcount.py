#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

def createWordCountDict(filename):
  """
  :param filename: path to 'filename' text file
  :return: word/count dict
  This function reads 'filename' text file and builds and returns a word/count dict for it
  All words in 'filename' shall be considered as lowercase, so 'The' and 'the' count as the same word.
  """
  fileObject = open(filename, 'rU')
  fileString = fileObject.read()
  listOfWordsInFilename = fileString.split()

  wordCountDict = {}
  for w in listOfWordsInFilename:
      w = w.lower()
      wkeep = ""
      for char in w:
          if char.isalpha():
              wkeep = wkeep + char
      if wkeep!="":
          if wkeep in wordCountDict:
              wordCountDict[wkeep] = wordCountDict[wkeep] + 1
          else:
              wordCountDict[wkeep] = 1

  return wordCountDict

def print_words(filename):
  """
  :param filename: path to 'filename' text file
  :return: None (printing function)
  function that counts how often each word (all considered as lowercase) appears in 'filename'
  (using function createWordCountDict) and prints (sorted by word) :
  word1 count1
  word2 count2
  ...
  """
  wordCountDict = createWordCountDict(filename)
  print('List of words in "'+str(filename)+'" with the number of times they appear :')
  for key in sorted(wordCountDict.keys()):
      print(key, wordCountDict[key])

  return


def print_top(filename, nb_top_common_words=20):
  """
  :param filename: path to 'filename' text file
  :param nb_top_common_words: number of top common words to display
  :return: None (printing function)
  function that counts how often each word (all considered as lowercase) appears in 'filename'
  (using function createWordCountDict) and prints top nb_top_common_words common words (sorted by reverse count) :
  word1 count1
  word2 count2
  ...
  """
  wordCountDict = createWordCountDict(filename)
  print('List of top '+str(nb_top_common_words)+' words in "' + str(filename) + '" with the number of times they appear :')
  list_of_top_common_words = sorted(wordCountDict.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
  #print(list_of_top_common_words)
  print('\n'.join([ str(myElement) for myElement in list_of_top_common_words[:nb_top_common_words]]))

  return

###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  if len(sys.argv) != 3:
    print('usage: ./wordcount.py {--count | --topcount} file')
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print('unknown option: ' + option)
    sys.exit(1)

if __name__ == '__main__':
  main()
