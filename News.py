import newspaper
from newspaper import Article
import nltk
from textblob import TextBlob

link = "https://www.businessinsider.com/tucker-carlson-text-its-not-how-white-men-fight-2023-5"

def getContent(link1):
    url = link1

    # Download the article
    article = Article(url)

    # Parse the article
    article.download()
    article.parse()
    article.nlp()
    
    # Print the article's title
    print(article.title)

    # Print the article's authors
    print(article.authors)

    # Print the published date of the article
    print(article.publish_date)

    # Print the article's content
    print(article.text)

    print("\nSummary:\n")
    print(article.summary)

    analysis = TextBlob(article.text)
    print (analysis.sentiment)

getContent(link)