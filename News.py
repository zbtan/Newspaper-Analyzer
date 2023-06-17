import newspaper
from newspaper import Article
import nltk
from textblob import TextBlob

url = 'https://www.hindustantimes.com/cricket/gt-vs-dc-live-score-ipl-2023-gujarat-titans-vs-delhi-capitals-todays-ipl-match-44-latest-scorecard-updates-101683021413230.html'

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

print("Summary:\n")
print(article.summary)

analysis = TextBlob(article.text)
print (analysis.sentiment)
