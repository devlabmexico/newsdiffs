from baseparser import BaseParser
import bs4

class ElSolDeMexicoParser(BaseParser):
    SUFFIX = ''
    domains = ['www.elsoldemexico.com.mx']
    feeder_pat   = '^https?://www.elsoldemexico.com.mx/[a-zA-Z0-9_\-]+(/[a-zA-Z0-9_\-]+)+\.(html)$'
    feeder_pages = [
                    'https://www.elsoldemexico.com.mx',
                    'https://www.elsoldemexico.com.mx/mexico',
                    'https://www.elsoldemexico.com.mx/mexico/justicia',
                    'https://www.elsoldemexico.com.mx/mexico/politica',
                    'https://www.elsoldemexico.com.mx/mexico/sociedad',
                    'https://www.elsoldemexico.com.mx/metropoli',
                    'https://www.elsoldemexico.com.mx/metropoli/cdmx',
                    'https://www.elsoldemexico.com.mx/metropoli/justicia',
                    'https://www.elsoldemexico.com.mx/metropoli/policia',
                    'https://www.elsoldemexico.com.mx/metropoli/valle-de-mexico',
                    'https://www.elsoldemexico.com.mx/republica',
                    'https://www.elsoldemexico.com.mx/republica/dos-mil-millas',
                    'https://www.elsoldemexico.com.mx/republica/justicia',
                    'https://www.elsoldemexico.com.mx/republica/politica',
                    'https://www.elsoldemexico.com.mx/republica/sociedad',
                    'https://www.elsoldemexico.com.mx/mundo',
                    'https://www.elsoldemexico.com.mx/finanzas',
                    'https://www.elsoldemexico.com.mx/finanzas/mercados',
                    'https://www.elsoldemexico.com.mx/finanzas/tecnologia',
                    'https://www.elsoldemexico.com.mx/analisis',
                    'https://www.elsoldemexico.com.mx/gossip',
                    'https://www.elsoldemexico.com.mx/gossip/celebridades',
                    'https://www.elsoldemexico.com.mx/gossip/omg',
                    'https://www.elsoldemexico.com.mx/circulos',
                    'https://www.elsoldemexico.com.mx/circulos/moda',
                    'https://www.elsoldemexico.com.mx/circulos/realeza',
                    'https://www.elsoldemexico.com.mx/circulos/turismo',
                    'https://www.elsoldemexico.com.mx/cultura',
                    'https://www.elsoldemexico.com.mx/cultura/arte',
                    'https://www.elsoldemexico.com.mx/cultura/cine',
                    'https://www.elsoldemexico.com.mx/cultura/exposiciones',
                    'https://www.elsoldemexico.com.mx/cultura/gastronomia',
                    'https://www.elsoldemexico.com.mx/cultura/literatura',
                    'https://www.elsoldemexico.com.mx/cultura/teatro',
                    'https://www.elsoldemexico.com.mx/doble-via',
                    'https://www.elsoldemexico.com.mx/doble-via/ciencia',
                    'https://www.elsoldemexico.com.mx/doble-via/ecologia',
                    'https://www.elsoldemexico.com.mx/doble-via/salud',
                    'https://www.elsoldemexico.com.mx/doble-via/virales',
                    'https://www.elsoldemexico.com.mx/deportes',
                    'https://www.elsoldemexico.com.mx/deportes/americano',
                    'https://www.elsoldemexico.com.mx/deportes/automovilismo',
                    'https://www.elsoldemexico.com.mx/deportes/en-el-ring',
                    'https://www.elsoldemexico.com.mx/deportes/futbol',
                    'https://www.elsoldemexico.com.mx/deportes/tenis',
                   ]

    def _parse(self, html):
        soup = bs4.BeautifulSoup(html)

        elt_title = soup.find('h1', class_="title")
        if elt_title is None:
            self.real_article = False
            return
        else:
            self.title = elt_title.getText()

        elt_body = soup.find('section', class_='col-sm-8')
        if elt_body is None:
            self.real_article = False
            return
        else: 
            elt_body_content = ''
            elt_body_ps = elt_body.findAll('p', class_=None)
            for p in elt_body_ps:
                elt_body_content = elt_body_content + "\n" + p.getText()

            elt_summary = soup.find('h3', class_='subtitle')
            if elt_summary is None:
                self.body = elt_body_content
            else:
                self.body = elt_summary.getText() + "\n" + elt_body_content

        
        elt_byline = soup.find('p', class_='byline')
        if elt_byline is None:
            self.byline = ''
        else:
            self.byline = elt_byline.getText()

        elt_date = soup.find('p', class_='published-date')
        if elt_date is None:
            self.date = ''
        else:
            self.date = elt_date.getText()
