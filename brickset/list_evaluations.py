"""
Gets the evaluations for all the courses
"""
import csv
from details import SearchPage, EvalsPage
from list_classes import getAllYaleCollegeClasses
from tqdm import tqdm

search = SearchPage()
evaluations = EvalsPage()


def getEvals(t):
    evals = evaluations.get(t['crn'])

    def get(obj, keys):
        bucket = {}
        for t in keys:
            if t in obj:
                bucket[t] = obj[t]
            else:
                bucket[t] = ""
        return bucket

    if 'course' in evals:
        return get(evals['course'], [
            'key', 'crn', 'title', 'instructordetail_html', 'eval_questions',
            'last_updated', 'narrative_questions', 'instructor_id'
        ])

    return get({}, [
        'key', 'crn', 'title', 'instructordetail_html', 'eval_questions',
        'last_updated', 'narrative_questions', 'instructor_id'
    ])


with open("all_evals.csv", 'w') as f:
    output = csv.writer(f)

    first = True
    for t in tqdm(getAllYaleCollegeClasses()):
        evals = getEvals(t)

        if first:
            output.writerow(evals.keys())
            first = False

        output.writerow(evals.values())
