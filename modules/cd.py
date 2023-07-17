from modules.library_item import LibraryItem


class CD():
    def __init__(self,title,subject,upc,artist):
        LibraryItem.__init__(self,title,upc,subject)
        self.artist = artist