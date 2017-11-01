from baseparser import BaseParser
import bs4

class TestParser(BaseParser):
    SUFFIX = ''
    domains = ['hugo.mecabotware.com']
    feeder_pat   = '^http://hugo.mecabotware.com/.+'
    feeder_pages = [ 'http://hugo.mecabotware.com/' ]

    def _parse(self, html):
        soup = bs4.BeautifulSoup(html)

        elt_title = soup.find('h2', itemprop="name")
        if elt_title is None:
            self.real_article = False
            return
        else:
            self.title = elt_title.getText()

        elt_body = soup.find('div', itemprop='articleBody')
        if elt_body is None:
            self.real_article = False
            return
        else: 
            self.body = elt_body.getText()

        
        elt_byline = soup.find('span', itemprop='author')
        if elt_byline is None:
            self.byline = ''
        else:
            self.byline = elt_byline.getText()

        elt_date = soup.find('span', itemprop='datePublished')
        if elt_date is None:
            self.date = ''
        else:
            self.date = elt_date.getText()

