import scrapy
from bs4 import BeautifulSoup, NavigableString
import random
import os


class BrickSetUtils:
    @staticmethod
    def getSubjectQuery(subject):
        return {
            'college': 'YC',
            'subject': subject,
            'courseNumber': '',
            'in': '',
            'keywords': '',
            'termCode': '01',
            'sort': 'Course Title'
        }

    @staticmethod
    def readCookies():
        dic = {}

        # paste your own cookies here!
        # Go to devtools, go to the "Network" tab, and refresh the page
        # When the page loads, you should see an index request (for the main
        # thing) Look at the request headers - cookies should be there!
        cookies = 'JSESSIONID=EF19D9BA28365412F2C8113A5E9457C2; _ga=GA1.2.695127647.1530509150; __cfduid=debcc9a14d002cfa00ab8644eba09984d1532318489; _gid=GA1.2.2095902581.1532407885'

        for t in cookies.split():
            t = t.replace(';', '').split('=')
            if len(t) == 2:
                cookie, value = t
                dic[cookie] = value
        return dic


class BrickSetSpider(scrapy.Spider):

    name = "brickset_spider"
    download_delay = 0.15    # 150 ms of delay

    def start_requests(self):
        start_urls = [
            'https://oce.app.yale.edu/oce-viewer/studentViewer/index'
        ]

        for url in start_urls:
            yield scrapy.Request(
                url,
                callback=self.parseSearchPage,
                cookies=BrickSetUtils.readCookies())

    def parseSearchPage(self, response):

        soup = BeautifulSoup(response.body, 'html.parser')
        class_dropdown = soup.find(id='subject')
        if class_dropdown is None:
            return

        for option in class_dropdown.children:
            if not isinstance(option, NavigableString):
                subCode = option['value']
                yield scrapy.FormRequest(
                    response.url,
                    formdata=BrickSetUtils.getSubjectQuery(subCode),
                    callback=self.parseSubject)

    def parseSubject(self, response):

        results_table = response.selector.xpath('//*[@id="course-list"]/div/table').extract_first()
        if results_table is None:
            return

        filename = "out{}.html".format(random.randint(10000, 100000))
        soup = BeautifulSoup(results_table, 'html.parser')

        with open(os.path.join('data/courselink-results', filename), "w") as f:
            f.write(soup.prettify())
