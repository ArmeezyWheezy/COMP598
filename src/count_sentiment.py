import json
import os
import math
import re
import csv
from csv import reader
from pathlib import Path

stowpath = os.path.join(Path(__file__).parents[1], "src", "stopwords.txt")
resultpath = os.path.join(Path(__file__).parents[1], "src", "sentiment.csv")
datapath = os.path.join(Path(__file__).parents[1], "data", "data.csv")
stopwords = []
stopfile = open(stowpath, "r").read().split("\n")
for i in stopfile:
    stopwords.append(i)





words = ['rules','flight', 'lockdowns', 'flying', 'sit', 'bla', 'sitting', 'jim', 'sing', 'risky', 'gmt', 'coronavirusupdate', 'coronaviruspandemic', 'died', 'coronavirus', 'total', 'australia', 'chaos', 'ab', 'black', 'team', 'union', 'died', 'philaunion', 'players', 'proud', 'psychological', 'issue', 'ill', 'profits', 'shot', 'booster', 'boosters','shots', 'vaccinated', 'unvaccinated', 'reactions', 'mrna', 'unvaxxed', 'jabs', 'omicron', 'african', 'variant', 'omnicron', 'cost', 'strain', 'rise', 'stocks', 'milder', 'reports', 'throat', 'breathe', 'symptoms', 'smell', 'fever', 'taste', 'lungs', 'goodness', 'headache', 'dry', 'tomorrow', 'tested', 'antigen', 'test', 'results', 'kinda', 'ur', 'antibody', 'absolute', 'hey', 'assess', 'amish', 'corvid', 'deer', 'george', 'killed', 'dems', 'centers', 'seh', 'ig']

j = len(words)

with open(resultpath, mode='w') as f:
    writer = csv.writer(f)

    i = 0

    for i in range(j):
        sent = [words[i],0,0,0]
        word = words[i]
        csvfile = open(datapath, "r", encoding="utf8")
        csv_reader = reader(csvfile)
        for i in csv_reader:
            a = re.sub("[^a-zA-Z0-9]", " ", i[3]).lower()
            j = a.split(" ")
            if word in j:
                if i[5] == "Postive":
                    sent[1] += 1
                elif i[5] == "Negative":
                    sent[2] += 1
                else:
                    sent[3] += 1
        writer.writerow (sent)
f.close()
