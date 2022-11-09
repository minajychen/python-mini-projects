#problem3
#jiang-ying mina chen
#custom scrabble text converter

import re
import sys

def scrabble_emoji():
    scrabble=False
    if sys.argv[0]=='problem3.py':
        scrabble=True
        del sys.argv[0]

        if scrabble:
            try:
                user=input(">")
                string=""
                for l in user:
                    string=string+":scrabble-"+l+":"
                    #regex blank substitution here
                string=string.replace(' ','blank')
                print(string)
            except (NameError, ValueError) as error:
                print(error)

if __name__ =='__main__':
    scrabble_emoji()