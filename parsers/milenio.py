from baseparser import BaseParser
import bs4

class MilenioParser(BaseParser):
    SUFFIX = ''
    domains = ['www.milenio.com/']
    feeder_pat   = '^http://www.milenio.com/[a-zA-Z0-9_\-]+(/[a-zA-Z0-9_\-]+)+\.(html)$'
    feeder_pages = [
                    'http://www.milenio.com',
                    'http://www.milenio.com/negocios',
                    'http://www.milenio.com/policia',
                    'http://www.milenio.com/cultura',
                    'http://www.milenio.com/salud',
                    'http://www.milenio.com/mujeres',
                    'http://www.milenio.com/cultura/laberinto',
                    'http://www.milenio.com/poligrafo',
                    'http://www.milenio.com/df',
                    'http://www.milenio.com/estadodemexico',
                    'http://www.milenio.com/monterrey',
                    'http://www.milenio.com/jalisco',
                    'http://www.milenio.com/laguna',
                    'http://www.milenio.com/tamaulipas',
                    'http://www.milenio.com/leon',
                    'http://www.milenio.com/salud-nutricion',
                    'http://www.milenio.com/tendencias',
                    'http://www.milenio.com/hey',
                    ]

    def _parse(self, html):
        soup = bs4.BeautifulSoup(html)

        elt_title = soup.find('h1', itemprop="name")
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
            elt_summary = soup.find('div', itemprop='description')
            if elt_summary is None:
                self.body = elt_body.getText()
            else:
                self.body = elt_summary.getText() + "\n" + elt_body.getText()

        
        elt_byline = soup.find('small', itemprop='author')
        if elt_byline is None:
            self.byline = ''
        else:
            self.byline = elt_byline.getText()

        elt_date = soup.find('time', itemprop='datePublished')
        if elt_date is None:
            self.date = ''
        else:
            self.date = elt_date.getText()

