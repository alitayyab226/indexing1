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

ps = PorterStemmer()



path = 'C:\\Users\\Tayyab Ali\\PycharmProjects\\indexing IR\\corpus\\'

i=0
files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '' in file:
            i = i+1
            files.append(os.path.join(r, file))

docid = open("docids.txt", "w+")
#termid = open("termids.txt", "w+")
termid = codecs.open("termids.txt", 'w+', encoding='utf-8',errors='ignore')
term_index = codecs.open("term_index.txt", 'w+', encoding='utf-8',errors='ignore')
delta_term_index = codecs.open("delta_encoding_term_inex.txt", 'w+', encoding='utf-8',errors='ignore')

hashmap = {}
hashmapTDWA = {}
hashmapW = {}
hashmapT = {}
#hashmap["word"] = "tayyab"
arr_list = []

i=0
k=0
l=0
for f in range(0,1000000):
    arr_list.append([])

for f in files:
    #print(os.path.basename(f))
    docid.write("%d\t%s\n" % (i, os.path.basename(f)))
    i=i +1
    #print(f)

    #file = open(f, "r")
    #file = open(f.title(), encoding="utf8")
    with codecs.open(f, 'r', encoding='utf-8',errors='ignore') as file:
        html = file.read()

    #print(file.read())



    #url = "http://news.bbc.co.uk/2/hi/health/2284783.stm"

    #file.close()


    #html = re.sub(r"\s+"," ", html, flags = re.I)
    html = html.lower().split("</head>", 1)[-1]
    #html = re.sub(r"\r\n", " ", html)

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
    #print(text)
    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)

    #print(text)
    text = re.sub(r"\d", " ", text)
    text = re.sub(r"[,@\'?/()|.$%_]|[-:&,<>]|[!-]", " ", text, flags=re.I)
    text = re.sub(r"\s+"," ", text, flags=re.I)
    text = re.sub(r"\s+[a-zA-Z]\s+", " ", text)

    text = text.lower()
    text = re.sub(r"\r\n", " ", text)
    #text = re.sub(r'[^A-Za-z]', '', text)
    whitelist = set('abcdefghijklmnopqrstuvwxyz ')
    text = ''.join(filter(whitelist.__contains__, text))
    #print(text)
    text = re.split(r"\s+", text)
    #print(text)

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
    j=0
    for word in list(text):  # iterating on a copy since removing will mess things up
        if word in stop_list:
            text.remove(word)
            j = j + 1
            #print(word)

    #print(text.__len__())
    #print(i)
    #print(text)

    #for w in text:
        #print(w, " : ", ps.stem(w))


    text = [ps.stem(word) for word in text]# for sentence in text]

    #ps.stem(text)

    #print(text.__len__())
    #text.append("tayyab")
    #text.append("tayyab")
    #print(text)
    temphash = {}
    for t in range(0, text.__len__()):
        temphash[text[t]] = 0
        #print(flags[t])



    for l in range(text.__len__()):
        try:
            hashmap.__getitem__(text[l])
            hashmap[text[l]] = hashmap[text[l]] + 1
            if temphash[text[l]] == 0:
                hashmapTDWA[text[l]] = hashmapTDWA[text[l]] + 1
                temphash[text[l]] = 1
                #print(flags.__getitem__(l))
            str = "{},{}"
            arr_list[hashmapT[text[l]]].append(str.format(i,l))
            #print(text[l])
        except:
            hashmap[text[l]] = 1
            if temphash[text[l]] == 0:
                hashmapTDWA[text[l]] = 1
                temphash[text[l]] = 1
                #print(flags.__getitem__(l))
            termid.write("%d\t%s\n" % (k, text[l]))
            hashmapW[k] = text[l]
            hashmapT[text[l]] = k;
            str = "{},{}"
            arr_list[k].append(str.format(i,l))
            k = k+1

    #print(arr_list[hashmap[text[1]]])
    #print(hashmap["diet"])

#print(hashmap)
#print(hashmapTDWA)
#print(hashmapW)
#print(hashmapT)

#print(arr_list[98].__len__())
#print(arr_list[98])

s=i
i=0
for i in range(0, hashmapT.__len__()):
    term_index.write("%i" %i)
    term_index.write("\t")
    term_index.write("%d" % hashmap[hashmapW[i]])
    term_index.write("\t")
    term_index.write("%d" % hashmapTDWA[hashmapW[i]])
    term_index.write("\t")
    j=0
    for j in range(0,(arr_list[i].__len__())):
        term_index.write("%s" % arr_list[hashmapT[hashmapW[i]]][j])
        term_index.write("\t")
    term_index.write("\n")

term_index.close()

for i in range(0, hashmapT.__len__()):
    delta_term_index.write("%i" %i)
    delta_term_index.write("\t")
    delta_term_index.write("%d" % hashmap[hashmapW[i]])
    delta_term_index.write("\t")
    delta_term_index.write("%d" % hashmapTDWA[hashmapW[i]])
    delta_term_index.write("\t")
    j=0
    str0 = "0"
    str1 = "1"
    for j in range(0,(arr_list[i].__len__())):
        if j==0:
            str0 = ("%s" % arr_list[hashmapT[hashmapW[i]]][j])
            delta_term_index.write("%s" % arr_list[hashmapT[hashmapW[i]]][j])
            delta_term_index.write("\t")
        if j>=1:
            str = "{},{}"
            str0 = re.split(r"[,]+", str0)
            str1 = ("%s" % arr_list[hashmapT[hashmapW[i]]][j])
            str1 = re.split(r"[,]+", str1)
            #print(str0[0])
            #print(str0[1])
            #print(str0[2])
            a = int(str1[0])-int(str0[0])
            b = int(str1[1])
            if a==0:
                b = int(str1[1])-int(str0[1])
            delta_term_index.write("%s" % str.format(a, b))
            delta_term_index.write("\t")
            str0 = arr_list[hashmapT[hashmapW[i]]][j]
    delta_term_index.write("\n")

delta_term_index.close()

termid.close()
docid.close()
