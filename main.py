from modules.book import Book
from modules.magazine import Magazine
from modules.dvd import DVD
from modules.cd import CD
from modules.catalog import Catalog
import json


book =[]
magazine =[]
dvd = []
cd = []
f = open(r"C:\Users\aryab\Documents\Belajar\Bootcamp Data Engineering\Project Digital Skola\Project 1\Project-1-Data-Engineering\files\catalog.json")
data_json = json.load(f)


for item in data_json:
    if item['source'] == 'book':
        book.append(Book(
            title=item['title'],
            subject=item['subject'],
            upc=item['upc'],
            issbn=item['issbn'],
            authors=item['authors'],
            dds_number=item['dds_number']
        ))
    if item['source'] == 'magazine':
        book.append(Magazine(
            title=item['title'],
            subject=item['subject'],
            upc=item['upc'],
            volume=item['volume'],
            issue=item['issue']
        ))
    if item['source'] == 'cd':
        book.append(CD(
            title=item['title'],
            subject=item['subject'],
            upc=item['upc'],
            artist=item['artist'],
        ))
    if item['source'] == 'DVD':
        book.append(DVD(
            title=item['title'],
            subject=item['subject'],
            upc=item['upc'],
            actor=item['actor'],
            director=item['director'],
            genre=item['genre']
        ))



catalog_all = [book,magazine,dvd,cd]

#search
input_search = str(input("Please input your Desired Title : "))
result=Catalog(catalog_all).search(input_search.lower())

if result:
    for index,result in enumerate(result):
        print(f'result ke - {index+1} | {result}' )
else:
    print("No Result")