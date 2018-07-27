import urllib.request as urllib
import json
import os, ssl


if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
    getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context



def get_market_data():
    print('Choose market. example: "BTC-OMG or USD-BTC"')
    market = input('> ')
    url = f"https://bittrex.com/api/v1.1/public/getticker?market={market}"
    json_obj = urllib.urlopen(url)
    data = json.load(json_obj)
    if data['success'] == False:
        print('Invalid input')
        get_market_data()
    else:
        #print(data)
        ask_data = data['result']['Bid']
        bid_data = data['result']['Ask']
        last_data = data['result']['Last']
        print(market)
        print(f'ASK: {ask_data}')
        print(f'BID: {bid_data}')
        print(f'LAST: {last_data}')
        get_market_data()


get_market_data()


