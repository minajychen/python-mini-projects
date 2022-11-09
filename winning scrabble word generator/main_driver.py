#problem1
#jiang-ying mina ahcne


import re
import words

def main():
    """Main driver for your program"""
    word_file=open("3_letter_words.txt",'r')
    content=word_file.read()
    content_lower=content.lower()
    formatted_lines=re.findall(r'[a-z]{3}', content_lower)
    word_values={}
    for i in formatted_lines:
        i=0
        while i < len(formatted_lines):
            value=words.points_for_letter(formatted_lines[i][0])+words.points_for_letter(formatted_lines[i][1])+words.points_for_letter(formatted_lines[i][2])
            word_values[formatted_lines[i]]=value
            i=i+1
    sorted_values=sorted(word_values.items(),key=lambda x:x[1], reverse=True)
    with open("3_letter_words_sorted.txt","w") as re_write:
        for tuple in sorted_values:
            re_write.write('%s-->%s\n' % tuple)
    re_write.close()
    return print("success")

if __name__ == '__main__':
    main()