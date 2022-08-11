import time
import requests
session_id = ''
url = ""
while True:
    print("searching..")
    headers = {
        'X-UT-SID': session_id
    }
    headers2 = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9,ar;q=0.8',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Host': 'utas.external.s2.fut.ea.com',
        'Origin': 'https://www.ea.com',
        'Pragma': 'no-cache',
        'Referer': 'https://www.ea.com/',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36',
        'X-UT-SID': session_id
    }
    r= requests.get(url,headers=headers)
    print(r.text)
    if 'timestamp' in r.text:
        id = r.text.split('"tradeId":')[1].split(",")[0]
        print(id)
        price = r.text.split('"buyNowPrice":')[1].split(',')[0]
        print(price)
        url2 = 'https://utas.external.s2.fut.ea.com/ut/game/fifa22/trade/' + id + '/bid'
        data = '{"bid":' + price + '}'
        r = requests.put(url2,data=data,headers=headers)
        print(r.text)
        if 'Permission Denied' in r.text:
            pass
        else:
            print('Bid completed successfully.. (Birthday Player Done)')
            break
    time.sleep(1)
