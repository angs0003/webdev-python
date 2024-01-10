import requests
from bs4 import BeautifulSoup

res = requests.get("https://www.codewithtomi.com/") # res is the response object
soup = BeautifulSoup(res.content, 'html.parser') # res.content is the HTML page

# print(soup.title.parent)

# Find tags in HTML pages below
s = soup.find_all('h2', class_='post-title') # returns a list

# Iterating through the result above 
for i in s:
    print(i.text) # print the text inside the tag
    print(i.a['href']) # print the link inside the tag
    print()