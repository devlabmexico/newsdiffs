from baseparser import BaseParser
import bs4

class ElUniversalParser(BaseParser):
    SUFFIX = ''
    domains = ['www.eluniversal.com.mx']
    feeder_pat   = '^http://www.eluniversal.com.mx/[a-zA-Z0-9_\-]+/[a-zA-Z0-9_\-]+'
    feeder_pages = [
                    'http://www.eluniversal.com.mx',
                    'http://www.eluniversal.com.mx/nacion',
                    'http://www.eluniversal.com.mx/mundo',
                    'http://www.eluniversal.com.mx/metropoli',
                    'http://www.eluniversal.com.mx/estados',
                    'http://www.eluniversal.com.mx/opinion',
                    'http://www.eluniversal.com.mx/cartera',
                    'http://www.eluniversal.com.mx/deportes',
                    'http://www.eluniversal.com.mx/espectaculos',
                    'http://www.eluniversal.com.mx/cultura',
                    'http://www.eluniversal.com.mx/periodismo-de-datos',
                    'http://www.eluniversal.com.mx/periodismo-de-investigacion',
                    'http://www.eluniversal.com.mx/tiempo-de-relojes',
                    'http://www.eluniversal.com.mx/ciencia-y-salud',
                    'http://www.eluniversal.com.mx/techbit',
                    'http://www.eluniversal.com.mx/menu',
                    'http://www.eluniversal.com.mx/de-ultima',
                    'http://www.eluniversal.com.mx/destinos',
                    'http://www.eluniversal.com.mx/autopistas',
                    'http://www.eluniversal.com.mx/english',
                    'http://www.eluniversal.com.mx/minuto-x-minuto'
                    ]

    def _parse(self, html):
        soup = bs4.BeautifulSoup(html)

        elt_title = soup.find('h1')
        if elt_title is None:
            self.real_article = False
            return
        else:
            self.title = elt_title.getText()

        elt_body = soup.find('div', class_='field-name-body')
        if elt_body is None:
            self.real_article = False
            return
        else: 
            elt_summary = soup.find('div', class_='field-name-field-resumen')
            if elt_summary is None:
                self.body = elt_body.getText()
            else:
                self.body = elt_summary.getText() + "\n" + elt_body.getText()

        
        elt_byline = soup.find('div', class_='field-item')
        if elt_byline is None:
            self.byline = ''
        else:
            self.byline = elt_byline.getText()

        elt_date = soup.find('div', class_='fechap')
        if elt_date is None:
            self.date = ''
        else:
            self.date = elt_date.getText()



