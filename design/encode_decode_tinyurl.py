"""Using increasing integers as codes."""


class TinyURL:
    def __init__(self):
        self.urls = []

    def encode(self, long_url):
        self.urls.append(long_url)
        return 'http://tinyurl.com/' + str(len(self.urls) - 1)

    def decode(self, short_url):
        return self.urls[int(short_url.split('/')[-1])]


"""Better way, using a random code of six digit/letter combinations.
If a long url is already stored, use the existing short url.
"""


class TinyURL:

    alphabet = string.ascii_letters + string.digits

    def __init__(self):
        self.urls = {}  # url -> code
        self.codes = {}  # code -> url

    def encode(self, long_url):
        if long_url not in self.urls:
            code = ''.join(random.choice(TinyURL.alphabet) for _ in range(6))
            if code not in self.codes:
                self.codes[code] = long_url
                self.urls[long_url] = code
        return 'http://tinyurl.com/' + self.urls[long_url]

    def decode(self, short_rl):
        return self.codes[short_url[-6:]]
