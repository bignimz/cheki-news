from flask import Flask, render_template
from ..requests import get_articles, get_articles_sos, get_headlines, get_sources
from . import main


@main.route('/')
def index():

    sources = get_sources()
    
    articles = get_articles('bbc-news')
    
    return render_template('index.html',articles=articles)


@main.route('/articles')
def articles():
    
    articles=get_articles(domain='bbc.com'+','+'cnn.com'+','+'techcrunch.com')
   
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



