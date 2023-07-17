from modules.book import Book
from modules.magazine import Magazine
from modules.cd import CD
from modules.dvd import DVD

class Catalog():
    def __init__(self,catalog=None):
        self.catalog = catalog


    def search(self,input_search): 
        list_hasil =[]
        for catalog in self.catalog:
            for item in catalog:
                if input_search in item.title.lower():
                    if type(item) == Magazine:
                        list_hasil.append("Title: " + item.title +" "+ "Volume : " +" "+ item.volume + "Issue : " +" "+ item.issue + "Type Catalog : Magazine")
                    elif type(item) == Book:
                        list_hasil.append("Title : " + item.title +" "+ "DDS Number : " +" "+ item.dds_number +" "+ "Type Catalog : Book")
                    elif type(item) ==DVD:
                        list_hasil.append("Title : " + item.title +" "+ "Genre : " + item.genre +" "+ "Type Catalog : DVD")
                    elif type(item) ==CD:
                        list_hasil.append("Title : " + item.title +" "+ "Artist : " + item.artist +" "+ "Type Catalog : CD")
                    else:
                        pass
        return list_hasil