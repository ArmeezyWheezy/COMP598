import json
import os
import math
import re
import csv
from csv import reader
from pathlib import Path

stowpath = os.path.join(Path(__file__).parents[1], "src", "stopwords.txt")
resultpath = os.path.join(Path(__file__).parents[1], "data", "sentiment.csv")
datapath = os.path.join(Path(__file__).parents[1], "data", "data.csv")
stopwords = []
stopfile = open(stowpath, "r").read().split("\n")
for i in stopfile:
    stopwords.append(i)


words = ["rules",
        "flight",
        "lockdowns",
        "flying",
        "sit",
        "bla",
        "sitting",
        "jim",
        "sing",
        "risky",
        "gmt",
        "coronavirusupdate",
        "coronaviruspandemic",
        "coronavirus",
        "23",
        "died",
        "total",
        "deaths",
        "australia",
        "chaos",
        "team",
        "union",
        "died",
        "philaunion",
        "players",
        "proud",
        "psychological",
        "issue",
        "ill",
        "profits",
        "shot",
        "booster",
        "boosters",
        "shots",
        "vaccinated",
        "unvaccinated",
        "reactions",
        "mrna",
        "unvaxxed",
        "jabs",
        "omicron",
        "african",
        "variant",
        "omnicron",
        "coronavirus",
        "cost",
        "strain",
        "rise",
        "stocks",
        "milder",
        "throat",
        "breathe",
        "symptoms",
        "smell",
        "fever",
        "taste",
        "lungs",
        "goodness",
        "headache",
        "dry",
        "tomorrow",
        "tested",
        "antigen",
        "test",
        "results",
        "kinda",
        "ur",
        "antibody",
        "absolute",
        "hey",
        "assess",
        "amish",
        "corvid",
        "deer",
        "george",
        "killed",
        "dems",
        "centers",
        "seh",
        "ig"]

k = len(words)

with open(resultpath, mode='w') as f:
    writer = csv.writer(f)
    writer.writerow(["Topic","Positive","Negative","Neutral"])

    i = 0

    for n in range(k):
        sent = [words[n],0,0,0]
        word = words[n]
        csvfile = open(datapath, "r", encoding="utf8")
        csv_reader = reader(csvfile)
        for i in csv_reader:
            if n < 10:
                if i[4] == "Restrictions": 
                    a = re.sub("[^a-zA-Z0-9]", " ", i[3]).lower()
                    j = a.split(" ")
                    if word in j:
                        if i[5] == "Positive":
                            sent[1] += 1
                        elif i[5] == "Negative":
                            sent[2] += 1
                        else:
                            sent[3] += 1
            elif 9<n<20:
                if i[4]== "Demography": 
                    a = re.sub("[^a-zA-Z0-9]", " ", i[3]).lower()
                    j = a.split(" ")
                    if word in j:
                        if i[5] == "Positive":
                            sent[1] += 1
                        elif i[5] == "Negative":
                            sent[2] += 1
                        else:
                            sent[3] += 1
            elif 19<n<30:
                if i[4] == "Impact":
                    a = re.sub("[^a-zA-Z0-9]", " ", i[3]).lower()
                    j = a.split(" ")
                    if word in j:
                        if i[5] == "Positive":
                            sent[1] += 1
                        elif i[5] == "Negative":
                            sent[2] += 1
                        else:
                            sent[3] += 1
            elif 29<n<40:
                if i[4] == "Vaccine":
                    a = re.sub("[^a-zA-Z0-9]", " ", i[3]).lower()
                    j = a.split(" ")
                    if word in j:
                        if i[5] == "Positive":
                            sent[1] += 1
                        elif i[5] == "Negative":
                            sent[2] += 1
                        else:
                            sent[3] += 1
            elif 39<n<50:
                if i[4] == "Variant":
                    a = re.sub("[^a-zA-Z0-9]", " ", i[3]).lower()
                    j = a.split(" ")
                    if word in j:
                        if i[5] == "Positive":
                            sent[1] += 1
                        elif i[5] == "Negative":
                            sent[2] += 1
                        else:
                            sent[3] += 1
            elif 49<n<60:
                if i[4] == "Symptoms":
                    a = re.sub("[^a-zA-Z0-9]", " ", i[3]).lower()
                    j = a.split(" ")
                    if word in j:
                        if i[5] == "Positive":
                            sent[1] += 1
                        elif i[5] == "Negative":
                            sent[2] += 1
                        else:
                            sent[3] += 1
            elif 59<n<70:
                if i[4] == "Testing":
                    a = re.sub("[^a-zA-Z0-9]", " ", i[3]).lower()
                    j = a.split(" ")
                    if word in j:
                        if i[5] == "Positive":
                            sent[1] += 1
                        elif i[5] == "Negative":
                            sent[2] += 1
                        else:
                            sent[3] += 1
            else:
                a = re.sub("[^a-zA-Z0-9]", " ", i[3]).lower()
                j = a.split(" ")
                if word in j:
                    if i[5] == "Positive":
                        sent[1] += 1
                    elif i[5] == "Negative":
                        sent[2] += 1
                    else:
                        sent[3] += 1
        writer.writerow (sent)
f.close()
