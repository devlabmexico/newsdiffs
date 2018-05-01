from baseparser import BaseParser, grab_url, concat
import bs4, re

class ExcelsiorParser(BaseParser):
    SUFFIX = ''
    domains = ['www.excelsior.com.mx']
    feeder_pat   = 'http:\/\/www.excelsior.com.mx(\/\/www.excelsior.com.mx)*\/[a-z]+\/[a-zA-Z0-9\_\-\/]+\/[a-zA-Z0-9\_\-\/]+([0-9\_\-\/]\.)*$'
    feeder_pages = ['http://www.excelsior.com.mx',
                    'http://www.excelsior.com.mx/nacional',
                    'http://www.excelsior.com.mx/nacional/elecciones-presidenciales',
                    'http://www.excelsior.com.mx/nacional/seguridad',
                    'http://www.excelsior.com.mx/nacional/estados',
                    'http://www.excelsior.com.mx/nacional/politica',
                    'http://www.excelsior.com.mx/politica',
                    'http://www.excelsior.com.mx/sociedad',
                    'http://www.excelsior.com.mx/global',
                    'http://www.excelsior.com.mx/dineroenimagen',
                    'http://www.excelsior.com.mx/comunidad',
                    'http://www.excelsior.com.mx/comunidad/seguridad',
                    'http://www.excelsior.com.mx/comunidad/gobierno-de-la-ciudad-de-mexico',
                    'http://www.excelsior.com.mx/comunidad/delegaciones',
                    'http://www.excelsior.com.mx/comunidad/reconstruccion',
                    'http://www.excelsior.com.mx/movilidad',
                    'http://www.excelsior.com.mx/expresiones',
                    'http://www.excelsior.com.mx/opinion',
                    'http://www.excelsior.com.mx/trending',
                    'http://www.excelsior.com.mx/nacional/elecciones-2018',
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
    @classmethod
    def feed_urls(cls):
        all_urls = []
        for feeder_url in cls.feeder_pages:
            html = grab_url(feeder_url)
            soup = cls.feeder_bs(html)

            # "or ''" to make None into str
            urls = [a.get('href') or '' for a in soup.findAll('a')]

            # If no http://, prepend domain name
            domain = '/'.join(feeder_url.split('/')[:3])
            urls = [url if '://' in url else concat(domain, url) for url in urls]

            all_urls = all_urls + [url for url in urls if
                                   re.search(cls.feeder_pat, url)]

        # Substitute urls that have http://www.excelsior.com.mx//www.excelsior.com.mx/
        angular_js_string = "http://www.excelsior.com.mx//www.excelsior.com.mx/"
        all_urls = [url if not angular_js_string in url else url.replace(angular_js_string, "http://www.excelsior.com.mx/") for url in all_urls]

        return all_urls