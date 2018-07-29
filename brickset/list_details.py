"""
Gets the details pages for all the courses
"""
import csv
from details import SearchPage, DetailsPage
from list_classes import getAllYaleCollegeClasses
from progressbar import ProgressBar


search = SearchPage()
details = DetailsPage()


def getDetails(class_result):
    deets = details.get(class_result)

    # these are really lengthy, haha
    for t in ['xlist', 'all_sections_remove_children']:
        del deets[t]

    if 'SYLLABUS' not in deets['resources']:
        deets['resources'] = ""

    return deets


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
