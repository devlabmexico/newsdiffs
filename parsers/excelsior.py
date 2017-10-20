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
