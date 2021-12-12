import json
import os
import math
import re
from csv import reader
from pathlib import Path

stowpath = os.path.join(Path(__file__).parents[1], "src", "stopwords.txt")
resultpath = os.path.join(Path(__file__).parents[1], "data", "result.json")
datapath = os.path.join(Path(__file__).parents[1], "data", "data.csv")
stopwords = []
stopfile = open(stowpath, "r").read().split("\n")
for i in stopfile:
    stopwords.append(i)

idf = {}
data = {'Restrictions': {}, 'Demography': {}, 'Impact': {}, 'Vaccine': {}, 'Variant': {}, 'Symptoms': {}, 'Testing': {},
        'Other': {}}
tf_data = {'Restrictions': {}, 'Demography': {}, 'Impact': {}, 'Vaccine': {}, 'Variant': {}, 'Symptoms': {},
           'Testing': {}, 'Other': {}}
idf_data = {'Restrictions': {}, 'Demography': {}, 'Impact': {}, 'Vaccine': {}, 'Variant': {}, 'Symptoms': {},
            'Testing': {}, 'Other': {}}
word_total = {'Restrictions': 0, 'Demography': 0, 'Impact': 0, 'Vaccine': 0, 'Variant': 0, 'Symptoms': 0, 'Testing': 0,
              'Other': 0}
tf_idf_data = {'Restrictions': {}, 'Demography': {}, 'Impact': {}, 'Vaccine': {}, 'Variant': {}, 'Symptoms': {},
               'Testing': {}, 'Other': {}}
word = {'Restrictions': {}, 'Demography': {}, 'Impact': {}, 'Vaccine': {}, 'Variant': {}, 'Symptoms': {},
               'Testing': {}, 'Other': {}}
result = {}

csvfile = open(datapath, "r", encoding="utf8")
csv_reader = reader(csvfile)

topic = ["Restrictions","Demography","Impact","Vaccine","Variant","Symptoms","Testing","Other"]
sentiment = ["Positive","Negative","Neutral"]


for i in csv_reader:
    category = i[4]
    a = re.sub("[^a-zA-Z0-9]", " ", i[3]).lower()
    j = a.split(" ")
    if i[5] not in word[category]:
        word[category][i[5]] = 1
    else:
        word[category][i[5]] += 1
    for line in j:
        if line != '':
            if line not in stopwords:
                if line in (data.get(category)):
                    data[category][line] += 1
                else:
                    data[category][line] = 1
        else:
            continue

for i in data:
    for j in data[i]:
        word_total[i] += data[i][j]

for i in data:
    for j in data[i]:
        tf_data[i][j] = data[i][j] / word_total[i]

for i in data:
    for j in data[i]:
        if j not in idf:
            idf[j] = 1
        else:
            idf[j] += 1

for i in data:
    for j in data[i]:
        idf_data[i][j] = math.log10(8 / idf[j])

for i in data:
    for j in data[i]:
        tf_idf_data[i][j] = tf_data[i][j] * idf_data[i][j]

for i in data:
    result[i] = sorted(tf_idf_data[i], key=tf_idf_data[i].get, reverse=True)[:int(10)]


with open(resultpath, "w") as f:
    json.dump(result, f, indent=4)


