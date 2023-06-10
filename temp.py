import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from collections import deque

def get_domain(url):
    Domain_name = ''
    x = url.split("/")
    
    if(x[0] == "https:" or x[0] == "http:"):
        x = x[2].split(".")
    else:
        x = x[0].split(".")
    if(len(x) == 2):
        Domain_name = x[0]
    else:
        Domain_name = x[1]
    return Domain_name

parent_dict = {}
def get_all_links(url):
   
    print("********************* Getting All The Links From the Site *********************")
    print()

    actual_domain=get_domain(url)
    all_links = set()
    queue_links=deque([])
    visited=set()

    all_links.add(url)
    queue_links.append(url)

    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
    
    while queue_links:

        url= queue_links.popleft()
        
        if url not in visited and get_domain(url) == actual_domain:
            
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')

            for anchor in soup.find_all('a'):

                href = anchor.get('href')

                if href and not (href.startswith("mailto:") or href.startswith("javascript:") or href.startswith('tel') or href.startswith('#')):

                    absolute_url = href

                    if not (absolute_url.startswith("http") or absolute_url.startswith("https")) :

                        absolute_url =urljoin(url, href)                 

                    if absolute_url not in parent_dict:
                        parent_dict[absolute_url] = set()

                    parent_dict[absolute_url].add(url)
                    all_links.add(absolute_url)
                    queue_links.append(absolute_url)

        visited.add(url)

    print("********************** All Links Are Fetched **********************")
    print(all_links,len(all_links))
    return all_links

get_all_links('https://www.thinkgroupy.com/')

print('parent ')
print(parent_dict)