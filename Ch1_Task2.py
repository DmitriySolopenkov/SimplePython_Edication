# Аналогично Ch1_Task1.py, но используя библиотеку requests
import requests
url = "https://gdata.youtube.com/feeds/api/standardfeeds/top_rated?alt=json"
response = requests.get(url)
data = response.json()
for video in data['feed']['entry'][0:6]:
print(video['title']['$t'])
