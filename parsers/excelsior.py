from baseparser import BaseParser
import bs4

class ExcelsiorParser(BaseParser):
    SUFFIX = ''
    domains = ['www.excelsior.com.mx']
    feeder_pat   = '^http://www.excelsior.com.mx/[a-z]+/20[0-9]{2}/[0-9]{2}/[0-9]{2}/[0-9]+'
    feeder_pages = ['http://www.excelsior.com.mx',
    				'http://www.excelsior.com.mx/nacional',
    				'http://www.excelsior.com.mx/global',
    				'http://www.excelsior.com.mx/dinero',
    				'http://www.excelsior.com.mx/comunidad',
    				'http://www.excelsior.com.mx/adrenalina',
    				'http://www.excelsior.com.mx/funcion',
    				'http://www.excelsior.com.mx/hacker',
    				'http://www.excelsior.com.mx/expresiones',
    				'http://www.excelsior.com.mx/opinion',
    				'http://www.excelsior.com.mx/videos']

    def _parse(self, html):
    	soup = bs4.BeautifulSoup(html)

    	self.title = soup.find('h1', class_='node-title').getText()

    	summary = soup.find('h2', class_='node-summary').getText()
    	article = soup.find('div', {'id' : 'node-article-body'}).getText()
    	self.body = summary + "\n" + article

    	self.byline = ''

    	self.date = soup.find('span', class_='imx-data-created').getText()
