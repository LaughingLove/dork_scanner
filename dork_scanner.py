#!/usr/bin/python

import argparse
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote

def google_search(query, pages):
    print(query)
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0'}
    req = requests.get('https://google.com/search?q='+ quote(query), headers=headers)
    soup = BeautifulSoup(req.text, 'html.parser')
    results = soup.find_all("cite", attrs={'class', 'iUh30'})
    #print(results)
    print(soup)
    for result in results:
        print(result.text)
    print("Found " + str(len(results)) + " results!")

def ddg_search(query, pages):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0'}
    req = requests.get('https://duckduckgo.com/html/?q={}'.format(quote(query)), headers=headers)
    
    soup = BeautifulSoup(req.text, 'html.parser')
    #print(soup)
    links = soup.find_all('a', {'class', 'result__url'})
    #format_links = []
    for link in links:
        import time
        time.sleep(1.5)
        print("----------------------------------------------------------------")
        print(link.text.strip())
    print("--------------")
    print("| "+str(len(links)) + " results! " + "|")
    print("--------------")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("Search", help="The search query")
    parser.add_argument("Engine", help="The search engine")
    parser.add_argument("-p", "--pages", help="The number of pages you want to search", type=int)
    args = parser.parse_args()

    query = args.Search
    engine = args.Engine
    pages = args.pages

    if engine.lower() == "google":
        google_search(query, pages)
    elif engine.lower() == "duckduckgo" or engine.lower() == "ddg":
        ddg_search(query, pages)

if __name__ == "__main__":
    main()