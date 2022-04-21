# Telegram search
Simple web scrapping to search from telegram

## Free API
- https://api.tufaah.repl.co/telegram-search/?type=videos&channel=funny&keyword=Nice
- https://api.tufaah.repl.co/telegram-search/?type=photos&channel=memes&keyword=a
- https://api.tufaah.repl.co/telegram-search/?type=links&channel=memes&keyword=a
- https://api.tufaah.repl.co/telegram-search/?type=files&channel=avira&keyword=python

## Search types
- Photos 
- Videos
- Links
- Files

## Help

install requirements
```
pip install -r requirements.txt
```

Example
```
( 1 ) Photos
( 2 ) Videos
( 3 ) Links
( 4 ) Files

 For what you want to search: 4
 Enter the channel username: avira
 Enter the keyword: python

output:
{'ok': True, 'results': [{'title': 'main.py', 'link': 'https://t.me/Avira/364'}, {'title': 'main.py', 'link': 'https://t.me/Avira/389'}, {'title': 'main.py', 'link': 'https://t.me/Avira/393'}, {'title': 'TeleX.py', 'link': 'https://t.me/Avira/401'}, {'title': 'yt_download.py', 'link': 'https://t.me/Avira/403'}, {'title': 'smdo.py', 'link': 'https://t.me/Avira/406'}, {'title': '7sim.py', 'link': 'https://t.me/Avira/415'}, {'title': 'IG.py', 'link': 'https://t.me/Avira/417'}, {'title': 'killer.py', 'link': 'https://t.me/Avira/422'}, {'title': 'raed.py', 'link': 'https://t.me/Avira/427'}, {'title': 'mrkzgulfup.py', 'link': 'https://t.me/Avira/430'}, {'title': 'Proxy.py', 'link': 'https://t.me/Avira/432'}, {'title': 'sc.py', 'link': 'https://t.me/Avira/439'}, {'title': 'Yahoo.py', 'link': 'https://t.me/Avira/447'}, {'title': 'TeleView.py', 'link': 'https://t.me/Avira/449'}, {'title': 'Tikify.py', 'link': 'https://t.me/Avira/454'}]}
```
