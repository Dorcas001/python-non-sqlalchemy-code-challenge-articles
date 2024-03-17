class Article:
    all = []

    def __init__(self, author, magazine, title):
        
        
        self.title = title
        self._author = author
        self._magazine = magazine
        self._title = title
        Article.all.append(self)

        # if not isinstance(title, str):
        #     raise ValueError("Title must be a string")
        # if len(title) < 5 or len(title) > 50:
        #     raise ValueError("Title must be between 5 and 50 characters")
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, new_title):
        if hasattr(self, '_title'):
            raise AttributeError("Title cannot be changed after instantiation")
        if not isinstance(new_title, str):
            raise ValueError("Title must be a string")
        if len(new_title) < 5 or len(new_title) > 50:
            raise ValueError("Title length must be between 5 and 50 characters")
        self._title = new_title

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, new_author):
        if isinstance(new_author, Author):
            self._author = new_author
        else:
            raise TypeError("Author must be of type Author")

    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, new_magazine):
        if isinstance(new_magazine, Magazine):
            self._magazine = new_magazine
        else:
            raise TypeError("Magazine must be of type Magazine")

        
class Author:
    def __init__(self, name):
        # self.name = name
        if not isinstance(name, str): # to check if the name is str
            raise TypeError("Name must be of type str")
        if len(name) == 0: # tocheck if name length is greater than
            raise ValueError("Name must be longer than 0 characters")
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if hasattr(self, '_name'):
            raise AttributeError("Cannot change author's name after instantiation")
        else:
            self._name = value
    def write_article(self, magazine, title):
        article = Article(self, magazine, title)
        self.articles_list.append(article)

    
    def articles(self):
        return self._articles    

    def magazines(self):
        return [article.magazine for article in self.articles]



    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self._articles.append(article)
        return article
   
    
    def topic_areas(self):
        articles = self.articles()  
        if not articles:
            return None
        return list(set(article.magazine.topic for article in articles))

class Magazine:
    all =[]
    def __init__(self, name, category):
        
        if not isinstance(name, str):
            raise TypeError("Name must be of type str")
        if 2 <=len(name) == 16:
           raise ValueError("Name must be between 2 and 16 characters")
        if len(category) == 0:
            raise ValueError("Category must be longer than 0 characters")
        self._name = name
        self._category = category
        self._articles = []
        # self.authors = {}
        self.published_articles = []

    def get_name(self):
        return self._name
    

    def articles(self):
        if not all(isinstance(article, Article) for article in self._articles):
            raise TypeError("Articles must be instances of the Article class")
        return self._articles

    @property
    def category(self):
        return self._category
    # def articles(self):
    #     return self.published_articles
    def add_article(self, article):
        self.published_articles.append(article)


    def contributors(self):
        authors = set()
        authors = []
        for article in self.published_articles:
            if article.author not in authors:
                authors.append(article.author)
        return authors

    def article_titles(self):
        if not self.articles:
            return None
        return [article.title for article in self.articles]


    def contributing_authors(self):
        authors_count = {}
        for article in self._articles:
            author = article.author
            if author not in authors_count:
                authors_count[author] = 1
            else:
                authors_count[author] += 1

        contributing_authors = [author for author, count in authors_count.items() if count > 2]

        return contributing_authors
# author_1 = Author("Carry Bradshaw") 
# print(author_1)
