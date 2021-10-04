import requests, time, json
from random import choice, randint

# Load urls from file
urls = []
with open('urls.txt', 'r') as urlfile:
    for url in urlfile.readlines():
        urls.append(url.strip('\n'))

# Load HTTP headers from file
headers = {}
with open('headers.json', 'r') as hdrfile:
    headers = json.loads(hdrfile.read())

print(f'Loaded {str(len(urls))} urls.')
while 1: # Infinite loop to randomly open sites, with random timeout
    try:
        headers['Referer'] = 'https://' + choice(urls)
        url = 'https://' + choice(urls)
        sleep = randint(3,7)
        print(f'Visiting {url}')
        req = requests.get(url, allow_redirects=False, timeout=3, headers=headers)
        print(f'Visited {url}, response code: {str(req.status_code)}')
        print(f'Sleeping for {str(sleep)} seconds.')
        time.sleep(sleep)

    except KeyboardInterrupt: exit()
    except: print('Exception ocurred!')
