import requests

h={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}
print(requests.get(' http://www.linkedin.com/in/ayush-kothiyal',headers=h).status_code)