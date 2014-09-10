# -*- coding: utf-8 -*-
"""
Created on Tue Sep  9 23:13:01 2014

@author: Samantha
"""

# modules to import
import sys
import time
import random
import string

# create a function to generate files with, say, 1000 lines
def makeRows(numrows, filename):
  start = time.time()

  # make the sets of all letters more accessible:
  letters = list(string.ascii_lowercase)
  LETTERS = list(string.ascii_uppercase)
    
  # write the new chunk of rows:
  ### NOTE:  should really check to see if that file exists already so it doesn't overwrite!!!
  with open(filename, 'a') as csvfile:
    write = csv.writer(csvfile)   #ADDED THIS LINE
    
    for i in range(numrows):
  
      # start by creating each line:
      numerics = [random.choice([0.1, 0.2, 0.3]) for x in range(97)] # numerics
      integer = random.choice([-1, 0, 1]) # integer
      factor = random.choice(LETTERS) # factor

      # for characters, generate random length then sample characters:
      charlen = random.randint(1, 10) # generates random integer, includes boundaries
      characters = ''.join([random.choice(letters) for x in range(charlen)])

      write.writerow(numerics + [integer] + [factor] + [characters])  #CHANGED THIS TO ALL LISTS

  print "Time to generate 10000 rows: ", time.time()-start, "sec"

  return


# the part that says what to do when the file is executed
def main():
  args = sys.argv[1:]
#  if len(args) != 2:
#     print "Usage:  --numrows --outfile"
  
#  numrows = args[0]
#  outfile = args[1]
  
  makeRows(1000, "1000.txt")
  makeRows(10000, "10000.txt")

if __name__ == '__main__':
  main()

