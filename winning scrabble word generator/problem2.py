#problem2
#jiang-ying mina achen
#this program includes a function that produces highest possible scrable scores from up to 7 letter tiles

import re 
import operator
import itertools
import words

scrabble_file=open("scrabble_list.txt",'r')
scrabble_content=scrabble_file.read()
scrabble_neutral=scrabble_content.lower()
scrabble_list=scrabble_neutral.split()
i=0
scrabble_tuples=[]
while i < 53901:
    splitted=tuple(list(scrabble_list[i]))
    scrabble_tuples.append(splitted)
    i+=1

def join_tuple_string(scrabble_tuples) -> str:
    return ''.join(scrabble_tuples)

result=list(map(join_tuple_string, scrabble_tuples))

def main():
    try:
        user_input=input("Enter each letter in your rack:")
        if re.search(r'^[a-zA-Z]{8,}$',user_input):
            print("please only enter 7 letters.")
        elif re.search(r'^[a-zA-Z]{,7}$',user_input) or re.search(r'^[a-zA-Z,]{,13}$', user_input) or re.search(r'^[a-zA-Z\s]{,13}$',user_input):
            if re.search(r'^[a-zA-Z,]{,13}$', user_input):
                user_input_clean=user_input.replace(',','')
            elif re.search(r'^[a-zA-Z\s]{,13}$',user_input):
                user_input_clean=user_input.replace(' ','')
            else:
                user_input_clean=user_input
            word_tuples=[]
            x=2
            while x <=7:
                word_list=list(itertools.combinations(list(user_input_clean),x))
                word_tuples.extend(word_list)
                x+=1
            word_list=list(map(join_tuple_string, word_tuples))
            print (word_list)
            temp_list=set(result)&set(word_list)
            clean_word_list=sorted(temp_list, key=lambda k: word_list.index(k))
            print(clean_word_list)
            scrabble_values={}      
            for word in clean_word_list:
                total_score=0
                for letter in word:
                    value=words.points_for_letter(letter)
                    total_score+=value
                scrabble_values[word]=total_score
            
            # here is a series of print statements that creates solutions aligned with the prompt's format
            _2_letter={key:val for key, val in scrabble_values.items() if len(key)==2}
            _2_letter_top15=dict(sorted(_2_letter.items(), key=operator.itemgetter(1), reverse=True)[:15])
            print ("2 letter words\n"+"-"*16)
            if bool(_2_letter_top15)==False:
                print("no words found")
            elif bool(_2_letter_top15)==True:
                for key in _2_letter_top15:
                    print("{}:{}".format(key, _2_letter_top15[key]))
            print("\n")
            _3_letter={key:val for key, val in scrabble_values.items() if len(key)==3}
            _3_letter_top15=dict(sorted(_3_letter.items(), key=operator.itemgetter(1), reverse=True)[:15])
            print ("3 letter words\n"+"-"*16)
            if bool(_3_letter_top15)==False:
                print("no words found")
            elif bool(_3_letter_top15)==True:
                for key in _3_letter_top15:
                    print("{}:{}".format(key, _3_letter_top15[key]))
            print("\n")
            _4_letter={key:val for key, val in scrabble_values.items() if len(key)==4}
            _4_letter_top15=dict(sorted(_4_letter.items(), key=operator.itemgetter(1), reverse=True)[:15])
            print ("4 letter words\n"+"-"*16)
            if bool(_4_letter_top15)==False:
                print("no words found")
            elif bool(_4_letter_top15)==True:
                for key in _4_letter_top15:
                    print("{}:{}".format(key, _4_letter_top15[key]))
            print("\n")
            _5_letter={key:val for key, val in scrabble_values.items() if len(key)==5}
            _5_letter_top15=dict(sorted(_5_letter.items(), key=operator.itemgetter(1), reverse=True)[:15])
            print ("5 letter words\n"+"-"*16)
            if bool(_5_letter_top15)==False:
                print("no words found")
            elif bool(_5_letter_top15)==True:
                for key in _5_letter_top15:
                    print("{}:{}".format(key, _5_letter_top15[key]))
            print("\n")
            _6_letter={key:val for key, val in scrabble_values.items() if len(key)==6}
            _6_letter_top15=dict(sorted(_6_letter.items(), key=operator.itemgetter(1), reverse=True)[:15])
            print ("6 letter words\n"+"-"*16)
            if bool(_6_letter_top15)==False:
                print("no words found")
            elif bool(_6_letter_top15)==True:
                for key in _6_letter_top15:
                    print("{}:{}".format(key, _6_letter_top15[key]))
            print("\n")
            _7_letter={key:val for key, val in scrabble_values.items() if len(key)==7}
            _7_letter_top15=dict(sorted(_7_letter.items(), key=operator.itemgetter(1), reverse=True)[:15])
            print ("7 letter words\n"+"-"*16)
            if bool(_7_letter_top15)==False:
                print("no words found")
            elif bool(_7_letter_top15)==True:
                for key in _7_letter_top15:
                    print("{}:{}".format(key, _7_letter_top15[key]))
            print("\n")
        else:
            print ("error")
    except (TypeError, NameError, ValueError) as error:
        print(error)

if __name__ == "__main__":
    main()