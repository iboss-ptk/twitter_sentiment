import json


def get_data_from_file(file_name):
    f = open(file_name, "r", encoding='utf-8')
    emo = dict()

    for line in f.readlines():
        sent, l = line.split("\t", 1)
        sent = int(sent)
        emo[sent] = [
            s[1]['geo']['coordinates']
            for s in json.loads(l) if s[1]['geo'] is not None
        ]

    return emo


def get_def(v):
    if v == -1:
        return "negative"
    if v == 0:
        return "neutral"
    return "positive"


prefx = "../reduced/"
file_list = [
    "four_seasons",
    "grand_hyatt",
    "marriott",
    "sheraton"
]

data = dict()

for f in file_list:
    file_name = prefx + f
    data[f] = get_data_from_file(file_name)


result = []

for e in range(-1, 2):
    result += [{
        "name": get_def(e),
        "radius": 5.5,
        "fillKey": str(e),
        "borderWidth": 1.5,
        "fillOpacity": 0.9,
        "latitude": coord[0],
        "longitude": coord[1]
    } for coord in data['grand_hyatt'][e]]

print(json.dumps(result))
