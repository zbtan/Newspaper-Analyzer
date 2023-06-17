import requests
import json

def getNews():
    headers = {'Authorization': '4a1881413b8143db95b834e4b976230d'}
    top_headlines = "https://newsapi.org/v2/top-headlines?"
    symbols = " "
    country = ['my']
    sources = ['bbc-news', 'business-insider', 'financial-post', 'google-news', 'reuters','nbc-news', 'techcrunch', 'the-wall-street-journal']
    sorby = "popularity"
    # set up the query parameters
    params= {
        'q': symbols,
        'apiKey': '4a1881413b8143db95b834e4b976230d',
        'sortBy': sorby,
        'language': 'en',
        'pageSize': 100,
        'page': 1
        }

    # send the request to the API and get the response
    response = requests.get(url=top_headlines, headers=headers, params=params)

    # convert the response to a JSON object
    output = response.json()

    # retrieve all articles from the response
    articles = output['articles']
    while 'next' in response.links.keys():
        response = requests.get(response.links['next']['url'], headers=headers, params=params)
        output = response.json()
        articles += output['articles']

    # print out all articles
    for article in articles:
        print(json.dumps(article, indent=4))

    # get the total number of results
    total_results = output['totalResults']
    print(f"Total Results: {total_results}")

def getByCategory():
    print("[1] Business\n[2] Entertainment\n[3] General\n[4] Health\n[5] Sport\n[6] Tecknology\n[7] Science\n")
    choose = input("\nChoose: ")

    category = " "

    if choose == '1':
         category = "business"
    elif choose == '2':
        category = "entertainment"
    elif choose == '3':
        category = "general"
    elif choose == '4':
        category = "health"
    elif choose == '5':
        category = "sports"
    elif choose == '6':
        category = "technology"
    elif choose == '7':
        category = "science"
    
    headers = {'Authorization': '4a1881413b8143db95b834e4b976230d'}
    top_headlines = "https://newsapi.org/v2/top-headlines?"
    symbols = " "
    country = ['my']
    sources = ['bbc-news', 'business-insider', 'financial-post', 'google-news', 'reuters','nbc-news', 'techcrunch', 'the-wall-street-journal']
    sorby = "popularity"
    # set up the query parameters
    params= {
        'q': symbols,
        'category': category,
        'apiKey': '4a1881413b8143db95b834e4b976230d',
        'sortBy': sorby,
        'language': 'en',
        'pageSize': 100,
        'page': 1
        }

    # send the request to the API and get the response
    response = requests.get(url=top_headlines, headers=headers, params=params)

    # convert the response to a JSON object
    output = response.json()

    # retrieve all articles from the response
    articles = output['articles']
    while 'next' in response.links.keys():
        response = requests.get(response.links['next']['url'], headers=headers, params=params)
        output = response.json()
        articles += output['articles']

    # print out all articles
    for article in articles:
        print(json.dumps(article, indent=4))

    # get the total number of results
    total_results = output['totalResults']
    print(f"Total Results: {total_results}")

def searchNews():
    search = input("Keyword of News: ")

    headers = {'Authorization': '4a1881413b8143db95b834e4b976230d'}
    top_headlines = "https://newsapi.org/v2/everything?"
    symbols = " "
    country = ['my']
    sources = ['bbc-news', 'business-insider', 'financial-post', 'google-news', 'reuters','nbc-news', 'techcrunch', 'the-wall-street-journal']
    sorby = "relevancy"
    # set up the query parameters
    params= {
        'q': search,
        'apiKey': '4a1881413b8143db95b834e4b976230d',
        'sortBy': sorby,
        'language': 'en',
        'pageSize': 100,
        'page': 1
        }

    # send the request to the API and get the response
    response = requests.get(url=top_headlines, headers=headers, params=params)

    # convert the response to a JSON object
    output = response.json()

    # retrieve all articles from the response
    articles = output['articles']
    while 'next' in response.links.keys():
        response = requests.get(response.links['next']['url'], headers=headers, params=params)
        output = response.json()
        articles += output['articles']

    # print out all articles
    for article in articles:
        print(json.dumps(article, indent=4))

    # get the total number of results
    total_results = output['totalResults']
    print(f"Total Results: {total_results}")

<<<<<<< HEAD
def searchNewsLink():
    search = input("Keyword of News: ")

    headers = {'Authorization': '4a1881413b8143db95b834e4b976230d'}
    top_headlines = "https://newsapi.org/v2/everything?"
    symbols = " "
    country = ['my']
    sources = ['bbc-news', 'business-insider', 'financial-post', 'google-news', 'reuters','nbc-news', 'techcrunch', 'the-wall-street-journal']
    sorby = "relevancy"
    # set up the query parameters
    params= {
        'q': search,
        'apiKey': '4a1881413b8143db95b834e4b976230d',
        'sortBy': sorby,
        'language': 'en',
        'pageSize': 100,
        'page': 1
        }

    # send the request to the API and get the response
    response = requests.get(url=top_headlines, headers=headers, params=params)

    # convert the response to a JSON object
    output = response.json()

    # retrieve all articles from the response
    articles = output['articles']
    while 'next' in response.links.keys():
        response = requests.get(response.links['next']['url'], headers=headers, params=params)
        output = response.json()
        articles += output['articles']

    # create a list to store the article links
    article_links = []

    # store only the article links in the list
    for article in articles:
        article_links.append(article['url'])

    # get the total number of results
    total_results = output['totalResults']
    print(f"Total Results: {total_results}")

    # return the list of article links
    return article_links

def getByCategoryLink():
    print("[1] Business\n[2] Entertainment\n[3] General\n[4] Health\n[5] Sport\n[6] Technology\n[7] Science\n")
    choose = input("\nChoose: ")

    category = ""

    if choose == '1':
         category = "business"
    elif choose == '2':
        category = "entertainment"
    elif choose == '3':
        category = "general"
    elif choose == '4':
        category = "health"
    elif choose == '5':
        category = "sports"
    elif choose == '6':
        category = "technology"
    elif choose == '7':
        category = "science"
    
    headers = {'Authorization': '4a1881413b8143db95b834e4b976230d'}
    top_headlines = "https://newsapi.org/v2/top-headlines?"
    symbols = " "
    country = ['my']
    sources = ['bbc-news', 'business-insider', 'financial-post', 'google-news', 'reuters','nbc-news', 'techcrunch', 'the-wall-street-journal']
    sorby = "popularity"
    # set up the query parameters
    params= {
        'q': symbols,
        'category': category,
        'apiKey': '4a1881413b8143db95b834e4b976230d',
        'sortBy': sorby,
        'language': 'en',
        'pageSize': 100,
        'page': 1
        }

    # send the request to the API and get the response
    response = requests.get(url=top_headlines, headers=headers, params=params)

    # convert the response to a JSON object
    output = response.json()

    # retrieve all articles from the response
    articles = output['articles']
    while 'next' in response.links.keys():
        response = requests.get(response.links['next']['url'], headers=headers, params=params)
        output = response.json()
        articles += output['articles']

    # create a list to store the article links
    article_links = []

    # store only the article links in the list
    for article in articles:
        article_links.append(article['url'])

    # get the total number of results
    total_results = output['totalResults']
    print(f"Total Results: {total_results}")

    # return the list of article links
    return article_links

def getNewsLink():
    headers = {'Authorization': '4a1881413b8143db95b834e4b976230d'}
    top_headlines = "https://newsapi.org/v2/top-headlines?"
    symbols = " "
    country = ['my']
    sources = ['bbc-news', 'business-insider', 'financial-post', 'google-news', 'reuters','nbc-news', 'techcrunch', 'the-wall-street-journal']
    sorby = "popularity"
    # set up the query parameters
    params= {
        'q': symbols,
        'apiKey': '4a1881413b8143db95b834e4b976230d',
        'sortBy': sorby,
        'language': 'en',
        'pageSize': 100,
        'page': 1
        }

    # send the request to the API and get the response
    response = requests.get(url=top_headlines, headers=headers, params=params)

    # convert the response to a JSON object
    output = response.json()

    # retrieve all articles from the response
    articles = output['articles']
    while 'next' in response.links.keys():
        response = requests.get(response.links['next']['url'], headers=headers, params=params)
        output = response.json()
        articles += output['articles']

    # create a list to store the article links
    article_links = []

    # store only the article links in the list
    for article in articles:
        article_links.append(article['url'])

    # get the total number of results
    total_results = output['totalResults']
    print(f"Total Results: {total_results}")

    # return the list of article links
    return article_links

def getNewsobject():
    headers = {'Authorization': '4a1881413b8143db95b834e4b976230d'}
    top_headlines = "https://newsapi.org/v2/top-headlines?"
    symbols = " "
    country = ['my']
    sources = ['bbc-news', 'business-insider', 'financial-post', 'google-news', 'reuters','nbc-news', 'techcrunch', 'the-wall-street-journal']
    sorby = "popularity"
    # set up the query parameters
    params= {
        'q': symbols,
        'apiKey': '4a1881413b8143db95b834e4b976230d',
        'sortBy': sorby,
        'language': 'en',
        'pageSize': 100,
        'page': 1
        }

    # send the request to the API and get the response
    response = requests.get(url=top_headlines, headers=headers, params=params)

    # convert the response to a JSON object
    output = response.json()

    # retrieve all articles from the response
    articles = output['articles']
    while 'next' in response.links.keys():
        response = requests.get(response.links['next']['url'], headers=headers, params=params)
        output = response.json()
        articles += output['articles']

    # return the list of articles
    return articles

def getByCategoryObject():
    print("[1] Business\n[2] Entertainment\n[3] General\n[4] Health\n[5] Sport\n[6] Technology\n[7] Science\n")
    choose = input("\nChoose: ")

    category = " "

    if choose == '1':
         category = "business"
    elif choose == '2':
        category = "entertainment"
    elif choose == '3':
        category = "general"
    elif choose == '4':
        category = "health"
    elif choose == '5':
        category = "sports"
    elif choose == '6':
        category = "technology"
    elif choose == '7':
        category = "science"
    
    headers = {'Authorization': '4a1881413b8143db95b834e4b976230d'}
    top_headlines = "https://newsapi.org/v2/top-headlines?"
    symbols = " "
    country = ['my']
    sources = ['bbc-news', 'business-insider', 'financial-post', 'google-news', 'reuters','nbc-news', 'techcrunch', 'the-wall-street-journal']
    sorby = "popularity"
    # set up the query parameters
    params= {
        'q': symbols,
        'category': category,
        'apiKey': '4a1881413b8143db95b834e4b976230d',
        'sortBy': sorby,
        'language': 'en',
        'pageSize': 100,
        'page': 1
        }

    # send the request to the API and get the response
    response = requests.get(url=top_headlines, headers=headers, params=params)

    # convert the response to a JSON object
    output = response.json()

    # retrieve all articles from the response
    articles = output['articles']
    while 'next' in response.links.keys():
        response = requests.get(response.links['next']['url'], headers=headers, params=params)
        output = response.json()
        articles += output['articles']

    # return the list of articles
    return articles

def searchNewsObject():
    search = input("Keyword of News: ")

    headers = {'Authorization': '4a1881413b8143db95b834e4b976230d'}
    top_headlines = "https://newsapi.org/v2/everything?"
    symbols = " "
    country = ['my']
    sources = ['bbc-news', 'business-insider', 'financial-post', 'google-news', 'reuters','nbc-news', 'techcrunch', 'the-wall-street-journal']
    sorby = "relevancy"
    # set up the query parameters
    params= {
        'q': search,
        'apiKey': '4a1881413b8143db95b834e4b976230d',
        'sortBy': sorby,
        'language': 'en',
        'pageSize': 100,
        'page': 1
        }

    # send the request to the API and get the response
    response = requests.get(url=top_headlines, headers=headers, params=params)

    # convert the response to a JSON object
    output = response.json()

    # retrieve all articles from the response
    articles = output['articles']
    while 'next' in response.links.keys():
        response = requests.get(response.links['next']['url'], headers=headers, params=params)
        output = response.json()
        articles += output['articles']

    # return the list of articles
    return articles
=======
searchNews()
>>>>>>> 0e5687678fcbc23b8b21e456b35a4dc7b07173a6
