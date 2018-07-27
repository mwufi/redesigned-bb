import json
import requests

url = 'https://courses.yale.edu/api/?page=fose&route=details'
headers = {
    'cookie':
    '_ga=GA1.2.695127647.1530509150; __cfduid=debcc9a14d002cfa00ab8644eba09984d1532318489; _gid=GA1.2.30667208.1532675253',
    'origin':
    'https://courses.yale.edu',
    'accept-encoding':
    'gzip, deflate, br',
    'accept-language':
    'en-US,en;q=0.9',
    'user-agent':
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    'content-type':
    'application/json',
    'accept':
    'application/json, text/javascript, */*; q=0.01',
    'referer':
    'https://courses.yale.edu/',
    'authority':
    'courses.yale.edu',
}


def genDetails(class_result):
    if 'code' not in class_result:
        print("no code!", class_result)
    if 'crn' not in class_result:
        print("no crn!", class_result)

    code_string = "code:{}".format(class_result['code'])
    crn_string = "crn:{}".format(class_result['crn'])

    details_query = {
        "group": code_string,
        "key": crn_string,
        "srcdb": "201803",
        "matched": crn_string
    }

    r = requests.post(url, data=json.dumps(details_query), headers=headers)
    return json.loads(r.text)
