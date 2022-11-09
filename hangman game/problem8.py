#jiang-ying mina ahcne
#problem 8

import random

#create a list of common words to be referenced in the hangman game
read=open("common_words.txt", 'r')
content=read.read()
content.strip()
x=content.lower()
cr_strings=x.split("\n")
#remove duplicates from cr_strings list
ulist=[]
[ulist.append(x) for x in cr_strings if x not in ulist]
ulist.sort()

#create a function that takes a random word from my created list of common words
def get_word():
    word=random.choice(ulist)
    return word.upper()

#create a function that plays out the hangman game
def play(word):
    word_completion="_"*len(word)
    guessed=False
    guessed_letters=[]
    guessed_words=[]
    tries=5
    print("Let's play hangman!")

    while not guessed and tries >0:
        guess=input("please guess a letter or word:").upper()
        if len(guess)==1 and guess.isalpha():
            if guess in guessed_letters:
                print("you already guessed the letter", guess)
            elif guess not in word:
                print(guess,"is not in the word.")
                tries-=1
                guessed_letters.append(guess)
            else:
                print("good job,", guess,"is in the word!")
                guessed_letters.append(guess)
                word_as_list=list(word_completion)
                indices=[i for i,letter in enumerate(word) if letter==guess]
                for index in indices:
                    word_as_list[index]=guess
                word_completion="".join(word_as_list)
                if "_" not in word_completion:
                    guessed==True
        elif len(guess)==len(word) and guess.isalpha():
            if guess in guessed_words:
                print("you already guessed the word",guess)
            elif guess!=word:
                print(guess,"is not the word.")
                tries-=1
                guessed_words.append(guess)
            else:
                guessed=Trueword_completion=word
        else:
            print("Not a valid guess.")
        print(tries)
        print(word_completion)
        print("\n")
    if guessed:
        print("congrats, you guessed the word! you win")
    else:
        print("sorry, you ran out of tries. the word was "+word+". Maybe next time!")

#define a main function
def main():
    word=get_word()
    play(word)
    while input("play again?(y/n)").upper()=="Y":
        word=get_word()
        play(word)

if __name__=="__main__":
    main()