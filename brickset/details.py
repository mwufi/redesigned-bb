import json
import requests

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


class URLPage:
    def __init__(self, url):
        self.url = url

    def genPayload(self, query_data):
        print('url page')
        pass

    def get(self, query_data, info=False):
        r = requests.post(
            self.url, data=self.genPayload(query_data), headers=headers)

        if info:
            print(r.elapsed)
            print(r.ok)
            print('Here are your results:')

        return json.loads(r.text)


class SearchPage(URLPage):
    def __init__(self):
        self.url = "https://courses.yale.edu/api/?page=fose&route=search"

    def genSamplePayload(self):
        return {
            'subject': 'USAF',
            'keyword': 'spectral',
            'instructor': 'foo',
            'col': 'DI',
            'overlap': '2344',
            'schedule_type_G': 'Y',
        }

    def genPayload(self, query):
        print('search')
        criteria = []
        for key, value in query.items():
            criteria.append({"field": key, "value": value})
        payload = {'other': {'srcdb': '201803'}, 'criteria': criteria}
        return json.dumps(payload)


class DetailsPage(URLPage):
    def __init__(self):
        self.url = 'https://courses.yale.edu/api/?page=fose&route=details'

    def verify(self, class_result):
        if 'code' not in class_result:
            print("no code!", class_result)
        if 'crn' not in class_result:
            print("no crn!", class_result)

    def genPayload(self, class_result):
        self.verify(class_result)

        code_string = "code:{}".format(class_result['code'])
        crn_string = "crn:{}".format(class_result['crn'])

        details_query = {
            "group": code_string,
            "key": crn_string,
            "srcdb": "201803",
            "matched": crn_string
        }
        return json.dumps(details_query)


class EvalsPage(URLPage):
    def __init__(self):
        self.url = 'https://courses.yale.edu/api/?page=fose&route=course-evals'

    def genPayload(self, crn):
        payload = {
            "srcdb": "201803",
            "crn": str(crn),
            "key": "c5e44e1eb7819fd5e9d69c01abb141cf85e687c5"
        }
        return json.dumps(payload)
