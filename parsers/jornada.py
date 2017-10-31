from baseparser import BaseParser
import bs4

class JornadaParser(BaseParser):
    SUFFIX = ''
    domains = ['www.jornada.unam.mx']
    feeder_pat   = '^http://www.jornada.unam.mx/ultimas/20[0-9]{2}/[0-9]{2}/[0-9]{2}/.*'
    feeder_pages = ['http://www.jornada.unam.mx/ultimas',
                    'http://www.jornada.unam.mx/ultimas/politica',
                    'http://www.jornada.unam.mx/ultimas/economia',
                    'http://www.jornada.unam.mx/ultimas/mundo',
                    'http://www.jornada.unam.mx/ultimas/estados',
                    'http://www.jornada.unam.mx/ultimas/capital',
                    'http://www.jornada.unam.mx/ultimas/sociedad-y-justicia',
                    'http://www.jornada.unam.mx/ultimas/ciencias',
                    'http://www.jornada.unam.mx/ultimas/cultura',
                    'http://www.jornada.unam.mx/ultimas/espectaculos',
                    'http://www.jornada.unam.mx/ultimas/deportes']

    def _parse(self, html):
        soup = bs4.BeautifulSoup(html)

        elt_title = soup.find('h1')
        if elt_title is None:
            self.real_article = False
            return
        else:
            self.title = elt_title.getText()

        elt_body = soup.find('div', id='content_nitf')
        if elt_body is None:
            self.real_article = False
            return
        else: 
            self.body = elt_body.getText()

        
        elt_byline = soup.find('span', class_='nitf_author')
        if elt_byline is None:
            self.byline = ''
        else:
            self.byline = elt_byline.getText()

        elt_date = soup.find('span', class_='nitf_date')
        if elt_date is None:
            self.date = ''
        else:
            self.date = elt_date.getText()
