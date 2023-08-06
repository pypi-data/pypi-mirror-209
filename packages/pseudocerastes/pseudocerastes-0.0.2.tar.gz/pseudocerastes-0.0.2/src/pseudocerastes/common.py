import urllib.request
from .core.parser import Parser
from .core.html import HtmlNode

def parse(data:str) -> HtmlNode:
    return Parser().parse(data)

def get(url:str):
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    return response.read().decode('latin-1')