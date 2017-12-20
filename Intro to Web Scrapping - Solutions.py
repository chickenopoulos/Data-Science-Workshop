-------Άσκηση-------

Να γίνουν scrap όλοι οι τίτλοι με τις τιμές που βρίσκονται στην πρώτη σελίδα

Λύση :

li = parser.find_all('li', {'class':'col-xs-6 col-sm-4 col-md-3 col-lg-3'})
li_length = len(li)
for index in range(li_length):
    print(li[index].find('h3').find('a')['title']) #prints the value of attribute "title" from li.h3.a

-------Άσκηση-------

1. Να φτιάξετε ένα pandas dataframe με όλα τα βιβλία από όλες τις σελίδες, 
   όπου οι στήλες θα είναι Όνομα, Τιμή, Διαθεσιμότητα, Βαθμολογία
2. Να βρείτε τη μέση τιμή της βαθμολογίας και της τιμής
3. Να τυπώσετε όλα τα βιβλία με 1 αστέρι βαθμολογία

---> tip: df = pd.DataFrame(list_of_lists, columns=list_with_headers)

Λύση :

import requests
import pandas as pd
from bs4 import BeautifulSoup

title = []
price = []
stock = [] #boolean or string? 
rating = []

#temp arrays
t = []
p = []
s = [] #boolean or string? 
r = []

for i in range(1, 51):

    #getting page content
    page_content = requests.get("http://books.toscrape.com/catalogue/page-"+str(i)+".html").content
    parser = BeautifulSoup(page_content, "html.parser")
    
    #getting the title
    li = parser.find_all('li', {'class':'col-xs-6 col-sm-4 col-md-3 col-lg-3'})
    li_length = len(li)
    for index in range(li_length):
        t.append(li[index].find('h3').find('a')['title'])
        
    #getting the price
    p_tag = parser.find_all('p', {'class':'price_color'})
    p_tag_length = len(p_tag)
    for index in range(p_tag_length):
        p.append(p_tag[index].text)
        
    #getting the stock availability
    p_tag = parser.find_all('p', {'class':'instock availability'})
    p_tag_length = len(p_tag)
    for index in range(p_tag_length):
        s.append(p_tag[index].text)
        
    #getting the rating
    p_tag = parser.find_all('p', {'class':'star-rating'})
    p_tag_length = len(p_tag)
    for index in range(p_tag_length):
        r.append(p_tag[index]['class'])
    
#splitting the titles - list of lists
for row in t:
    #split_list = row.split(',')
    title.append(row) #replace row with split_list

#splitting the prices - list of lists
for row in p:
    #split_list = row.split(',')
    price.append(row) #replace row with split_list
    
#splitting the stock availabilities - list of lists
for row in s:
    #making it clearer
    if row == '\n\n    \n        In stock\n    \n':
        row = 'In stock'
    else:
        row = 'Not in stock'
    #splitting
    #split_list = row.split(',')
    stock.append(row) #replace row with split_list
    
#splitting the ratings - list of lists
temp = []
for row in r:
    temp.append(row[1])

for row in temp:
    #split_list = row.split(',')
    rating.append(row) #replace row with split_list
    
#converting rating to integers
i = 0
for row in rating:
    if row == 'One':
        rating[i] = 1
        i += 1
    elif row == 'Two':
        rating[i] = 2
        i += 1
    elif row == 'Three':
        rating[i] = 3
        i += 1
    elif row == 'Four':
        rating[i] = 4
        i += 1
    elif row == 'Five':
        rating[i] = 5
        i += 1
#converting price to floats
i = 0
for row in price:
    price[i] = float(row[1:])
    i += 1
#creating the dataframe

#dictionary
d = {}
d['title'] = title
d['price'] = price
d['stock'] = stock
d['rating'] = rating
    #or
#list
list_of_lists = []
list_of_lists.append(title)
list_of_lists.append(price)
list_of_lists.append(stock)
list_of_lists.append(rating)

#zip(*list_of_lists) -->should reverse rows to columns and vice versa, but doesnt work in Python 3.xxx

df = pd.DataFrame.from_dict(d)

#Μέση τιμή βαθμολογίας και τιμής
print("Μέση τιμή : %.2f"  % df['price'].mean())
print("Μέση βαθμολογία : " + str(df['rating'].mean()))
print("------------------------")

#Όλα τα βιβλία με 1 αστέρι βαθμολογία

#shape is (1000,4)
books = 0
for i in range(1000):
    if(int(df.loc[i]['rating']) == 1):
        print(df.loc[i]['title'])
        books += 1
print("----------------------------------------------")
print("Total books with 1 star rating : " + str(books))
