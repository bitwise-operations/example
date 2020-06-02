import requests
from bs4 import BeautifulSoup, SoupStrainer

class SeachUrl():

    def all_url_page(self, url):
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser', parse_only=SoupStrainer('a'))
        all_url = [link['href'] for link in soup if link.has_attr('href')]
        
        return all_url
    
    def status_page(self, list_url):
        result = {}
        for url in list_url:
            try:
                r = requests.get(url)
            except requests.exceptions.MissingSchema:
                url = 'https://www.google.com' + url
                r = requests.get(url)
            result[url] = r.status_code
        return result
