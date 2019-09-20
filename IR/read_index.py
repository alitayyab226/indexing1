import numpy as np
import os
import numpy as np
import sys
import urllib
from bs4 import BeautifulSoup
import re
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import codecs


lines = [line.rstrip('\n') for line in open('C:\\Users\\Tayyab Ali\\PycharmProjects\\indexing IR\\termids.txt')]

for i in range(0,lines.__len__()):
    lines[i] = lines[i].split("\t")

val = input("Enter your value: ")
a=0

j=1
for i in range(0, lines.__len__()):
    if lines[i].__getitem__(1) == val:
        a = int(lines[i][0])

print(a)
lines1 = [line.rstrip('\n') for line in open('C:\\Users\\Tayyab Ali\\PycharmProjects\\indexing IR\\delta_encoding_term_inex.txt')]
for i in range(0,lines1.__len__()):
    lines1[i] = lines1[i].split("\t")

print("String %s" %val)
print("Term id %s" %lines1[a][0])
print("Total frequency %s" %lines1[a][1])
print("Number of documents containing term %s" %lines1[a][2])
