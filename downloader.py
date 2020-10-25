import requests
from bs4 import BeautifulSoup
import re

schedule = requests.get('https://oneforest.net/dd_dn/4039')
schedule_html = schedule.text

soup = BeautifulSoup(schedule_html, 'html.parser')
scr = soup.find_all('a', {'class': 'ab-link'})
for index in scr:
      try:
            value = index.attrs['href']
            regex = re.compile('[a-z]+')
            match = regex.findall(value)
            if match[0] == 'module':
                  adress = value
                  break
      except:
            pass
final = 'https://oneforest.net' + adress
print(final)
