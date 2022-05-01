class Sources:
    '''
    Function to create news sources
    '''
    def __init__(self, name, description, url):
        self.name=name,
        self.description=description
        self.url=url
        
        
class Articles:
    '''
    Function to create news articles
    '''
    def __init__(self, source, author, title, description, url, urlToImage, publishedAt):
        self.source = source
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt