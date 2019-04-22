import requests
from bs4 import BeautifulSoup
import json 
from pprint import pprint
url = "https://www.imdb.com/india/top-rated-indian-movies/"

# Task 1 completed
def scrape_top_list():
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    Title = soup.title
    print (Title)
   
    movei_detail = []

    tbody = soup.find('tbody', class_ = "lister-list")
    main = tbody.findAll("tr")

    for i in main:
        dictionry = {}
        name = i.find("td", class_="titleColumn").a.getText()
        year = i.find("span", class_= "secondaryInfo").getText()
        rank = i.find("td", class_= "ratingColumn imdbRating").getText()
        link = i.find("a", href = True )
        
        links = "https://www.imdb.com"+link['href']
        
        dictionry['name']=name
        dictionry['year']=year
        dictionry['rank']=float(rank)
        dictionry['link']=links
        
        movei_detail.append(dictionry)
        with open('movie_data.json', 'w') as outfile:
            json.dump(movei_detail, outfile)
    return (movei_detail)
scrapped = scrape_top_list()
print (scrapped)

# Task 2 completed
def group_by_year():
    with open ('movie_data.json', 'r') as json_file:
        data = json.load(json_file)
    a = {}
    for i in data:
        year = i['year']
        if year not in a:
            a[year] = []
        a[year].append(i)

        with open('year_collection.json', 'w') as outfile:
            json.dump(a, outfile)
    return a,"---------------------------"
print(group_by_year())

# Task 3 
def group_by_decade():
    with open ('movie_data.json', 'r') as json_file:
        data = json.load(json_file)
    





    









