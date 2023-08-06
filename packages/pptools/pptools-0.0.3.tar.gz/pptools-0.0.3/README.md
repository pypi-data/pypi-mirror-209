PyParsTools - is an auxiliary module for writing parsers. It has built-in examples of different types of parsers, creating headers, installing all the necessary modules and getting the soup object in one line. Below are examples of usage:

```python
from pptools.pptools import getSoup

headers = {'User-agent': 'Mozilla 5.0'}
soup = getSoup(url='https://sunlight.net/catalog', headers=headers).requests()
```

In addition to requests, the request can also be made via urllib3, Selenium and aiohttp



As mentioned earlier, this module is able to write the basics of 3 types of parsers for you - standard, asynchronous, browser-based. All parsers are created in your directory as .py files.
```python
from pptools.pptools import Parsers

Parsers.getRequestsParser()
Parsers.getAsyncioParser()
Parsers.getSeleniumParser()
```

Finally, my module can install all the libraries necessary for parsing itself and create a dictionary of headers for autofication on the site.

```python
from pptools.pptools import Helper

Helper.installAll()
headers = Helper.getHeaders()
Helper.aboutStatusCode(status_code=403)
#Says what to do when receiving different responses from the site
Helper.download_photo('url-to-your-photo')
#Downloads the photo from the link
```