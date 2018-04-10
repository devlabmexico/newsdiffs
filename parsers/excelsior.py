from baseparser import BaseParser
import bs4

class ExcelsiorParser(BaseParser):
    SUFFIX = ''
    domains = ['www.excelsior.com.mx']
    feeder_pat   = '^http:\/\/www.excelsior.com.mx\/[a-z]+\/[a-zA-Z0-9_\-\/]+\/[0-9]+'
    feeder_pages = ['http://www.excelsior.com.mx',
                    'http://www.excelsior.com.mx/nacional',
                    'http://www.excelsior.com.mx/global',
                    'http://www.excelsior.com.mx/dineroenimagen',
                    'http://www.excelsior.com.mx/comunidad',
                    'http://www.excelsior.com.mx/adrenalina',
                    'http://www.excelsior.com.mx/funcion',
                    'http://www.excelsior.com.mx/hacker',
                    'http://www.excelsior.com.mx/expresiones',
                    'http://www.excelsior.com.mx/opinion',
                    'http://www.excelsior.com.mx/trending',
                    'http://www.excelsior.com.mx/nacional/elecciones-2018',
                    'http://www.excelsior.com.mx/trump/una-nueva-era',
                    'http://www.excelsior.com.mx/medio-ambiente',
                    'http://www.excelsior.com.mx/viral',
                    'http://www.excelsior.com.mx/videos']

    def _parse(self, html):
        soup = bs4.BeautifulSoup(html)

        elt_title = soup.find('h1', class_="node-title")
        if elt_title is None:
            self.real_article = False
            return
        else:
            self.title = elt_title.getText()

        elt_body = soup.find('div', id='node-article-body')
        if elt_body is None:
            self.real_article = False
            return
        else: 
            elt_summary = soup.find('h2', class_='node-summary')
            if elt_summary is None:
                elt_summary = soup.find('h4', class_='node-summary')
                if elt_summary is None:
                    self.body = elt_body.getText()
                else:
                    self.body = elt_summary.getText() + "\n" + elt_body.getText()
            else:
                self.body = elt_summary.getText() + "\n" + elt_body.getText()

        self.byline = ''

        elt_date = soup.find('span', class_='imx-data-created')
        if elt_date is None:
            self.date = ''
        else:
            self.date = elt_date.getText()
