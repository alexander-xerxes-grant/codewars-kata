import tldextract

def url_parser(url: str) -> str:
    result = tldextract.extract(url).domain
    return result



print(url_parser("http://www.google.com"))