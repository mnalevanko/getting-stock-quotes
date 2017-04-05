import requests
import re
from bs4 import BeautifulSoup

def get_stock_price_from_wsj(ticker, opening_default = 0):
    '''Returns a tuple: opening price, high, low, close, volume.

    Since the WSJ web does not provide opening prices, the tuple will have
    a pre-defined default value.
    '''
    def _get_price(the_class):
        paragraph = soup.find_all('p', class_=the_class)
        return float(paragraph[0].get_text())

    # Make sure the symbol is lower case
    ticker = ticker.lower()
    url_base = 'https://www.wsj.com/search/term.html?KEYWORDS='
    url_appendix = ticker
    url = url_base + url_appendix

    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'}

    r = requests.get(url, headers=headers)
    content = r.text
    soup = BeautifulSoup(content, 'lxml')

    last_price = _get_price("last")
    high_price = _get_price("high")
    low_price = _get_price("low")

    paragraphs_vol = soup.find_all('p', class_='volume')
    volume = int(paragraphs_vol[0].get_text().replace(',',''))

    return opening_defaul, high_price, low_price, last_price, volume

if __name__ == '__main__':

    symbol = 'EDU'
    _, high_p, low_p, last_p, vol = get_stock_price_from_wsj(symbol)
    print('Ticker: {}\nLast price: {}\nIntraday high: {}\nIntraday low: {}\nVolume: {}'.format(symbol, last_p, high_p, low_p, vol))
