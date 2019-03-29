import warc
from bs4 import BeautifulSoup

def get_text_from_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup.get_text()



