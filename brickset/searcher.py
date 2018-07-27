import json
import requests
from details import genDetails

url = "https://courses.yale.edu/api/?page=fose&route=search"
headers = {
    'cookie':
    '_ga=GA1.2.695127647.1530509150; __cfduid=debcc9a14d002cfa00ab8644eba09984d1532318489',
    'origin':
    'https://courses.yale.edu',
    'accept-encoding':
    'gzip,',
    'accept-language':
    'en-US,en;q=0.9',
    'user-agent':
    'Mozilla/5.0',
    'content-type':
    'application/json',
    'accept':
    'application/json,',
    'referer':
    'https://courses.yale.edu/',
    'authority':
    'courses.yale.edu'
}

# a sample query might look like this {
#     'subject': 'USAF',
#     'keyword': 'spectral',
#     'instructor': 'foo',
#     'col': 'DI',
#     'overlap': '2344',
#     'schedule_type_G': 'Y',
# }


def genPayload(query):
    criteria = []
    for key, value in query.items():
        criteria.append({"field": key, "value": value})
    payload = json.dumps({'other': {'srcdb': '201803'}, 'criteria': criteria})
    # print('payload:', payload)
    return payload


def process(response):
    t = json.loads(response.text)
    if 'results' in t:
        for i, r in enumerate(t['results']):
            print(i, json.dumps(r))
            print()

        # gen the details of the first result
        print(genDetails(t['results'][0]))

    else:
        print(t)

payload = genPayload({'subject': 'AFST'})
r = requests.post(url, data=payload, headers=headers)
print(r.elapsed)
print(r.ok)
print('Here are your results:')

process(r)
