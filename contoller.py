
from bs4 import BeautifulSoup
import requests
import json

list_products=list()

def scrap():
   
    scaping_pages("https://webscraper.io/test-sites/e-commerce/allinone/phones/touch")
    scaping_pages("https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops")
    scaping_pages("https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets")

    with open('data/data.json','w') as file:
         json.dump(list_products, file, indent=4)  



def scaping_pages(website):
    url=website
    page= requests.get(url)
    soup=BeautifulSoup(page.content, 'lxml')

    category= soup.find('h1', class_='page-header')
    img= soup.find_all('img', class_='img-responsive')
    title= soup.find_all('a', class_='title')
    price= soup.find_all('h4', class_='price')
    description= soup.find_all('p', class_='description')
    
    for i in range(0 ,len(title), 1):
       
       product={
            'Category':category.get_text(),
            'Title':title[i].get_text(),
            'Price':price[i].get_text(),
            'Description':description[i].get_text(),
            'Img':img[i].get('src'),
        }
       list_products.append(product)
   

  

