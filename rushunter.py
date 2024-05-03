import time
from html_table_parser.parser import HTMLTableParser
import urllib.request
import io

def url_get_contents(uri):
    req = urllib.request.Request(url=uri)
    f = urllib.request.urlopen(req)
    return f.read()

baseUrl = "https://pfq.eltafez.com/pkrs"
baseClicklist = "https://pokefarm.com/users/"
