#problem5
#jiang-ying mina chen

#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  name_strings=[]
  f=open(filename, 'r')
  text=f.read()

  year_line=re.search(r'Popularity\sin\s(\d{4})', text)

  if not year_line:
    print("error - couldn't find the year")
    sys.exit(1)

  year=year_line.group(1)

  name_strings.append(year)

  tuples=re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', text)

  names_to_rank={}

  for rank_tuple in tuples:
    (rank, boyname, girlname)=rank_tuple

    if boyname not in names_to_rank:
      names_to_rank[boyname]=rank
    if girlname not in names_to_rank:
      names_to_rank[girlname]=rank

  sorted_names=sorted(names_to_rank.keys())

  for name in sorted_names:
    name_strings.append(name+" "+names_to_rank[name])
  
  return name_strings


def main():
  """this main function parses out command line behavior"""
  args = sys.argv[1:]

  if not args:
    print ('usage: [--summaryfile] file [file ...]')
    sys.exit(1)

  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  for filename in args:
    name_strings=extract_names(filename)

    text='\n'.join(name_strings)

    if summary:
      sumf=open(filename+'.summary','w')
      sumf.write(text+'\n')
      sumf.close()
    else:
      print (text)
  
if __name__ == '__main__':
  main()