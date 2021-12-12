import json
import os
import math
import re
from csv import reader
from pathlib import Path

stowpath = os.path.join(Path(__file__).parents[1], "src", "stopwords.txt")
resultpath = os.path.join(Path(__file__).parents[1], "src", "result.json")
datapath = os.path.join(Path(__file__).parents[1], "data", "data.csv")
stopwords = []
stopfile = open(stowpath, "r").read().split("\n")
for i in stopfile:
    stopwords.append(i)


csvfile = open(datapath, "r", encoding="utf8")
csv_reader = reader(csvfile)

topic = ["Restrictions","Demography","Impact","Vaccine","Variant","Symptoms","Testing","Other"]
sentiment = ["Positive","Negative","Neutral"]


result = {"Positive":0,"Negative":0,"Neutral":0}
top = input("Enter the topic(Restrictions,Demography,Impact,Vaccine,Variant,Symptoms,Testing,Other)\t")
word = input("Enter word\t")
for i in csv_reader:
    a = re.sub("[^a-zA-Z0-9]", " ", i[3]).lower()
    j = a.split(" ")
    if word in j:
        result[i[5]] += 1

print(result)
