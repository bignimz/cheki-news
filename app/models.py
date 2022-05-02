class Sources:
    '''
    Function to create news sources
    '''
    def __init__(self, id, name, description, url):
        self.id = id,
        self.name=name,
        self.description=description
        self.url=url
        
        
class Articles:
    '''
    Function to create news articles
    '''
    def __init__(self, title, description, url, urlToImage, publishedAt):
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt