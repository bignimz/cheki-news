from flask import Flask, render_template
from ..request import get_Articles, get_articles_sos, get_headlines, get_sources
from . import main


@main.route('/')
def index():

    sources = get_sources()
    
    articles = get_Articles(domain='bbc.com'+','+'cnn.com'+','+'techcrunch.com')
    
    return render_template('index.html',source=source,articles=articles)


@main.route('/articles')
def articles():
    
    articles=get_Articles(domain='bbc.com'+','+'cnn.com'+','+'techcrunch.com')
   
    return render_template('articles.html',articles=articles)


@main.route('/sources')
def source():
    
    sources=get_sources()
   
    return render_template('sources.html',articles=sources)


@main.route('/top-headlines')
def headlines():
   
    articles=get_headlines()
    
    # return render_template('articles.html',articles=articles)
    return render_template('articles.html',articles=articles)


# @main.route('/sources/<a>')
# def source_list(a):
#     a=re.sub(r'[^\w]', ' ', a)
#     a=a.strip()

#     print(a)
#     a=re.sub(' +', ' ', a)
#     a=a.split(" ")
#     joinsource='-'.join(a)
#     articles=get_articles_sos(joinsource)
#     return render_template('listfromsos.html',articles=articles)