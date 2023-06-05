class Book(object):
    title="Unknown"
    
    def __init__(self,title,author,pages=0):
        self.title=title
        self.pages=pages
        self.author=author
        
    def __str__(self):
         return "Book: "+self.title+" by "+self.author