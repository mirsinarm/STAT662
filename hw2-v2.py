# f0.csv:  1000 rows
# f1.csv:  0.01 G (where G = 16 for me)
# f2.csv:  0.1 G
# f3.csv:  0.2 G
# f4.csv:  0.6 G
# f5.csv:  2 G

# each line should have:
#   97 numeric values (sampled from 0.1, 0.2, 0.3)
#   1 integer value (sampled from -1, 0, 1) # should be column 98
#   1 factor value (sampled from letters) # column 99
#   1 unique character column (up to 10 characters total) # column 100

# memory guidelines:
#   double:  8 bytes
#   integer:  4 bytes
#   character:  1 byte per character

# SO ...
#   each row is 8*97 + 4*1 + 1*1 + 10*1 = 791 bytes
#   1000 rows = 791000 bytes = 0.791 MB

# 1.  Have it as a function



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
    for i in range(numrows):
  
      # start by creating each line:
      numerics = [random.choice([0.1, 0.2, 0.3]) for x in range(97)] # numerics
      integer = random.choice([-1, 0, 1]) # integer
      factor = random.choice(LETTERS) # factor

      # for characters, generate random length then sample characters:
      charlen = random.randint(1, 10) # generates random integer, includes boundaries
      characters = ''.join([random.choice(letters) for x in range(charlen)])

      csvfile.write(str(numerics) + ',' + str(integer) + ',' + str(factor) + ',' + characters + '\n')

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










