from urllib.parse import urlparse, urlsplit


def url_parser(url: str) -> str:
    return url.split("//")[-1].split("www.")[-1].split(".")[0]


print(url_parser("www.google.com"))
print(url_parser("http://google.com"))
print(url_parser("google.com"))
print(url_parser("https://www.google.co.uk"))
