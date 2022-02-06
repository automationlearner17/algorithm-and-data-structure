#!/usr/bin/python3

def load_numbers(filetxt):
  ar = []
  file = open(filetxt,'r')
  readfile = file.readlines()
# read = file.read()
#  print (read)
  for line in readfile:
   ar.append(int(line))
  return ar
