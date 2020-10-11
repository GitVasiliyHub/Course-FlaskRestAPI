from urllib.parse import urljoin

import requests

URL = 'http://localhost:5000'

if __name__ == "__main__":
    r = requests.get(url=urljoin(URL, "/books/"))
    print(r.text)



