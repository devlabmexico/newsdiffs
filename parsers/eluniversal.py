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
