import numpy as np
import os
import sys
import urllib
from bs4 import BeautifulSoup
import re

path = 'C:\\Users\\Tayyab Ali\\PycharmProjects\\indexing IR\\corpus\\'

i=0
files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '' in file:
            i = i+1
            files.append(os.path.join(r, file))

for f in files:
    print(f)

file = open(f, "r")
#print(file.read())


#url = "http://news.bbc.co.uk/2/hi/health/2284783.stm"
html = file.read()
file.close()


#html = re.sub(r"\s+"," ", html, flags = re.I)
html = html.lower().split("</head>", 1)[-1]

#print(html[1])
#html = re.sub(r"\s+[a-zA-Z]\s+", " ", html)

#html.split("body")[0]

#html = re.sub("[WARC1.0@*&?].*[head@*&?]", "", html)

#html = re.sub(r"\d", "", html)
#html = re.sub("|", "", html)

#html = re.sub(r'\bdbo\.\w+_fn\b', '', html)

soup = BeautifulSoup(html, 'html.parser')

# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out

# get text
text = soup.get_text()

# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text = '\n'.join(chunk for chunk in chunks if chunk)

text = re.sub(r"\d", "", text)
text = re.sub(r"[,@\'?/()|.$%_]|[-:&]", "", text, flags=re.I)
text = re.sub(r"\s+"," ", text, flags=re.I)
text = re.sub(r"\s+[a-zA-Z]\s+", " ", text)
text = text.lower()
text = re.split(r"\s+", text)

#print(text)




stop_list = []

with open('stoplist.txt', "r") as f:
    stop_list = f.read().split()



#if any(word in contents for word in text):
#    text.remove(contents)

#print(text.__len__())
#print(text[0])
#print(stop_list[1])

#print(text)
i=0
for word in list(text):  # iterating on a copy since removing will mess things up
    if word in stop_list:
        text.remove(word)
        i = i + 1
        #print(word)

#print(text.__len__())
#print(i)
print(text)