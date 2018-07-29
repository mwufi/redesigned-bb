"""
Gets the details pages for all the courses
"""
import csv
from details import SearchPage, DetailsPage
import time

search = SearchPage()
details = DetailsPage()


def getAllYaleCollegeClasses():
    t = search.get({'col': 'YC'})
    if 'results' in t:
        for result in t['results']:
            yield result


def getDetails(class_result):
    deets = details.get(class_result)

    # these are really lengthy, haha
    for t in ['xlist', 'all_sections_remove_children']:
        del deets[t]

    if 'SYLLABUS' not in deets['resources']:
        deets['resources'] = ""

    return deets


class ProgressBar:
    def __init__(self, total):
        self.width = 50
        self.total = total

        self.start()

    def start(self):
        self.start = time.time()
        self.i = 0

    def update(self, number):
        ratio = int(number) / self.total
        elapsed = time.time() - self.start
        eta = elapsed / ratio

        arrow = "=" * int(ratio * self.width) + "=>"
        self.i += 1
        if self.i % 10 == 0:
            print(arrow + "{} eta: {}".format(self.i, eta))


U = ProgressBar(3700)
with open("all_details.csv", 'w') as f:
    output = csv.writer(f)

    first = True
    for t in getAllYaleCollegeClasses():
        course_details = getDetails(t)

        if first:
            output.writerow(course_details.keys())
            first = False

        output.writerow(course_details.values())
        U.update(course_details['key'])
