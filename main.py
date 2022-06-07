import os
def reading():
  with open("words.txt") as f:
    total = 0
    for a in f:
      print(a.strip())
      word_list = a.split()
      print(word_list)
      numWords = len(word_list)
      total += numWords
      print(total)

def start():
  print("Opening 'words.txt'.")
  reading()
start()