import json
from details import SearchPage, EvalsPage, DetailsPage

search = SearchPage()
details = DetailsPage()
evaluations = EvalsPage()


def foo(obj, keys):
    for k in keys:
        if k in obj:
            print(k, ':', obj[k])


t = search.get({'subject': 'afst'})
if 'results' in t:
    for class_result in t['results']:
        # foo(class_result, ['code', 'crn', 'title'])
        print(json.dumps(class_result, indent=2, sort_keys=True))

        deets = details.get(class_result)
        print(json.dumps(deets, indent=2, sort_keys=True))

        # foo(deets, ['description'])

        evals = evaluations.get(class_result['crn'])
        if 'course' in evals:
            print(json.dumps(evals, indent=2, sort_keys=True))
            # foo(evals['course'], ['eval_questions'])
            # foo(evals['course'], ['narrative_questions'])
