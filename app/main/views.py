from flask import Flask, render_template
from ..requests import get_articles, get_headlines, get_sources
from . import main


@main.route('/')
def index():

    sources = get_sources()
    
    # articles = get_articles('cnn')
    
    return render_template('index.html',articles=sources)


# @main.route('/bbc')
# def bbc():

#     # sources = get_sources()

#     articles = get_articles('bbc')

#     return render_template('bbc.html', articles=articles)



@main.route('/articles')
def articles():
    
    articles=get_articles(domain='bbc.com'+','+'cnn.com'+','+'techcrunch.com')
   
    return render_template('articles.html',articles=articles)


@main.route('/sources')
def source():
    
    sources = get_sources()
    articles = get_articles('cnn')
   
    return render_template('sources.html',articles=articles)


@main.route('/top-headlines')
def headlines():
   
    articles=get_headlines()
    
    return render_template('articles.html',articles=articles)



