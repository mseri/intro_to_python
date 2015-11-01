from __future__ import print_function
import random
import sys

nonword = "\n"
w = nonword
gram = 4
n = gram + 1

# GENERATE TABLE
table = {}

for line in sys.stdin:
  ngrams = (line[i:i+n] for i in range(len(line) - n))
  for ngram in ngrams:
      w = ngram[0:n-1]
      l = ngram[-1]
      table.setdefault( w, [] )
      table[w].append(l)

table.setdefault( w, [] )
table[w].append(nonword) # Mark the end of the file

# GENERATE OUTPUT
w = random.choice(table.keys())

maxwords = 100

for i in xrange(maxwords):
    newletter = random.choice(table[w])
    if newletter == nonword: sys.exit()
    print(newletter, end="")
    w = w[1:] + newletter

print()