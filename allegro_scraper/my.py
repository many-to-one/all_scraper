import requests, re
from bs4 import BeautifulSoup

d = requests.get("https://free-proxy-list.net/")
soup = BeautifulSoup(d.content, 'html.parser')
td_elements = soup.select('.fpl-list .table tbody tr td')
ips = []
ports = []
for j in range(0, len(td_elements), 8):
    ips.append(td_elements[j].text.strip())
    ports.append(td_elements[j + 1].text.strip())

print('####ips#####', ips)
print('####ports#####', ports)