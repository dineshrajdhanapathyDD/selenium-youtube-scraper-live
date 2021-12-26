import requests

from bs4 import BeautifulSoup

#does not execute js
response = requests.get(YOUTUBE_TRENDING_URL)
print('status code', response.status_code)

#print('Output', response.text[:1000])

with open('trending.html', 'w') as f:
  f.write(response.text)

doc = BeautifulSoup(response.text, 'html.parser')
print('page title:', doc.title.text)

#find all the video divs

video_divs = doc.find_all('div', class_='ytd-video-renderer')
print(f'Found {len(video_divs)} videos')