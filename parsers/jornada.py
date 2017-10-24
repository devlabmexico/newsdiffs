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

        self.title = soup.find('h1').getText()

        self.body = soup.find('div', {'id' : 'content_nitf'}).getText()

        self.byline = soup.find('span', class_='nitf_author').getText()

        self.date = soup.find('span', class_='nitf_date').getText()
