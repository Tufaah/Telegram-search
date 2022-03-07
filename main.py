from requests import get
from bs4 import BeautifulSoup
from re import findall

# Simple web scrapping to search from telegram
# Coded By: ( https://github.com/Tufaah / https://t.me/Tufaah )
# My telegram channels:  ( https://t.me/avira / https://t.me/API_J )


def get_photos():
    photos = list()
    results = get(f'https://t.me/s/{channel}?q={search}').text
    regex = findall(
        r'<a class="tgme_widget_message_photo_wrap [0-9_-]+ [0-9_-]+" href="([A-Za-z0-9_/:.-]+)" style="width:([0-9]+px);background-image:url\(\'([A-Za-z0-9_/:.-]+)', results)
    for r in regex: photos.append({'link': r[0], 'width': r[1], 'photo': r[2]})
    return {'ok': True, 'results': photos if photos else 'Cant find any thing!'}


def get_videos():
    videos = list()
    results = get(f'https://t.me/s/{channel}?q={search}').content
    soup = BeautifulSoup(results, "lxml")

    link = soup.find_all("a", {"class": "tgme_widget_message_video_player blured js-message_video_player"})
    for l in range(len(link)): videos.append(link[l].attrs['href'])
    return {'stats': 'ok', 'results': videos if videos else 'Cant find any thing!'}


def get_files():
    texts, urls, mix = list(), list(), list()
    results = get(f"https://t.me/s/{channel}?q={search}").content
    soup = BeautifulSoup(results, "html.parser")

    text = soup.find_all("a", {"class": "tgme_widget_message_document_wrap"})
    for i in range(len(text)):
        texts.append(str(text[i].text).strip().split('\n')[0])
        urls.append(str(text[i].attrs['href']).strip().split('\n')[0])

    for i in range(len(urls)): mix.append({'title': texts[i], 'link': urls[i]})
    return {'ok': True, 'results': mix if mix else 'Cant find any thing!'}


def get_links():
    links = list()
    results = get(f'https://t.me/s/{channel}?q={search}').content
    soup = BeautifulSoup(results, "lxml")

    link = soup.find_all("a", {"class": "tgme_widget_message_link_preview"})
    for l in range(len(link)): links.append(link[l].attrs['href'])

    return {'ok': True, 'results': links if links else 'Cant find any thing!'}


print('''
 ( 1 ) Photos
 ( 2 ) Videos
 ( 3 ) Links
 ( 4 ) Files
''')

select = str(input(' For what you want to search: ')).strip()
channel = input(' Enter the channel username: ').strip().replace('@', '')
search = input(' Enter the keyword: ').strip()
if select == '1': print(get_photos())
elif select == '2': print(get_videos())
elif select == '3': print(get_links())
elif select == '4': print(get_files())
else: print(f' [X] Wrong number selected!')

