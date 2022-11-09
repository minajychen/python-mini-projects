#problem4
#jiang-ying mina chen
#this is a command line program that fetches the top new headlines or search for a particular subject
#using openNewsAPI. 

import requests
import json
import dateutil.parser

def print_news(url):
    r=requests.get(url)
    json_data=r.json()

    status=json_data["status"]
    total_results=json_data["totalResults"]
    articles=json_data["articles"]

    print("Status:"+status)
    print("Total Results:", total_results)
    print("-"*20)

    for article in articles[:10]:
        newdate=dateutil.parser.parse(article['publishedAt'])
        print("*", article['title'],newdate.date())
        print("\t",article['description'])
        print("-"*20+"\n")
    
    print("Would you like to find more news articles?[y/n]")
    end_input=input(">>>")
    if end_input=="y":
        main()

def top_headlines():
    print("""
    Select which category would you like to headlines for:   
    [1] business   
    [2] entertainment   
    [3] general   
    [4] health   
    [5] science   
    [6] sports   
    [7] technology""")
    user_input=input(">>>")
    try:
        if user_input=="1":
            url= "https://newsapi.org/v2/top-headlines?category=business&apiKey=a4b1546a9d4a43768b8e7bf6b7349fbf"
        elif user_input=='2':
            url= "https://newsapi.org/v2/top-headlines?category=entertainment&apiKey=a4b1546a9d4a43768b8e7bf6b7349fbf"
        elif user_input=='3':
            url= "https://newsapi.org/v2/top-headlines?category=general&apiKey=a4b1546a9d4a43768b8e7bf6b7349fbf"
        elif user_input=='4':
            url= "https://newsapi.org/v2/top-headlines?category=health&apiKey=a4b1546a9d4a43768b8e7bf6b7349fbf"
        elif user_input=='5':
            url= "https://newsapi.org/v2/top-headlines?category=science&apiKey=a4b1546a9d4a43768b8e7bf6b7349fbf"
        elif user_input=='6':
            url= "https://newsapi.org/v2/top-headlines?category=sports&apiKey=a4b1546a9d4a43768b8e7bf6b7349fbf"
        elif user_input=='7':
            url= "https://newsapi.org/v2/top-headlines?category=technology&apiKey=a4b1546a9d4a43768b8e7bf6b7349fbf"
        print_news(url)
    except (UnboundLocalError, TypeError, NameError) as error:
        print("error. try again.")
        main()
   
def search_word():
    print("Enter your search term:")
    search_input=input(">>>")
    url="https://newsapi.org/v2/everything?q={}&apiKey=a4b1546a9d4a43768b8e7bf6b7349fbf".format(search_input)
    print_news(url)

def main():
    print("Welcome to Command Line News!")
    print("Please make a choice: [1] Top headlines [2] Search")
    user_choice=input(">>>")
    if user_choice=='1':
        top_headlines()
    elif user_choice=='2':
        search_word()


if __name__ =='__main__':
    main()