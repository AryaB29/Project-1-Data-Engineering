from modules.library_item import LibraryItem

class DVD():
    def __init__(self,title,subject,upc,actor,director,genre):
        LibraryItem.__init__(self,title,upc,subject)
        self.actor = actor
        self.director = director
        self.genre = genre
        