"""
Gets the list of all Yale college classes from the search page
"""
import csv
from details import SearchPage

search = SearchPage()


def getAllYaleCollegeClasses():
    t = search.get({'col': 'YC'})
    if 'results' in t:
        for result in t['results']:
            yield result


with open("all.csv", 'w') as f:
    output = csv.writer(f)

    first = True
    for t in getAllYaleCollegeClasses():
        if first:
            print(t.keys())
            output.writerow(t.keys())
            first = False

        print(t.values())
        output.writerow(t.values())
