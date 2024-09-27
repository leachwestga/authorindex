# create the paperlist.txt file

import csv
import sys

file = open('authorlist.csv')
reader = csv.reader(file)
author={}

for line in reader:
    print(line)
    author[int(line[0])] = line[1].strip()
    if (len(line)>2):
        author[int(line[0])] += ", " + line[2].strip()
    if (len(line)>3):
        author[int(line[0])] += ", " + line[3].strip()

##print(author[371])
##sys.exit()

reverse = {}
for i in author.keys():
    reverse[author[i].strip()]=i

print("********************")

def openauthor(number):
    authorfile = "authorfiles/file" + str(number) +".txt"
    print("Open Author: ", end="")
    print(authorfile)
    f = open(authorfile, "r")
    filetext= f.read();
    filetext = filetext.replace("<li class=fragment>","<li>")
    filetext = filetext.replace('<li class="fragment">',"<li>")
    items = filetext.split("<li>")
    print(items)
    items.pop(0)
    name = items.pop(0).strip()[0:-5].strip();

    print("ITEMS")
    print(items)
    

    print(len(items))
    for i in range(len(items)):
        items[i]=items[i].strip()

##    for i in range(len(items)):
##        papers.append[items[i]]
        if (items[i][0]=="("):
            closingparen = items[i].index(")") + 1
            items[i]=items[i][closingparen:]
            items[i]=items[i].strip()
            items[i]=items[i].replace("\n","")
        print(items[i])
    f.close()
    return([name,items])

#a = openauthor(14)

f1 = open("paperlist.txt","a");

for ii in range(1,2093):    
    a = openauthor(ii)
    print("-------------")
    print("authorfile: "+str(ii))
    print(a[0])
    print("searching for author")
    print(a[0].strip())
    authorid= reverse[a[0].strip()]
    print("\n")
    for i in a[1]:
    ##    print("-->" + i)
        paper = i
        title= i[:i.index("<a hre")-1]
        if (title[-1]==','):
            title=title[:-1]
        volume = i[i.index("Vol")+3:i.index("</a>")].strip()
    ##    print(title, end=", Vol ")
    ##    volume = i[i.index("Vol")+3:i.index("</a>")].strip()
    ##    print(volume, end = ";;")
    ##    print(authorid)

        line = title + ";;" + volume + ";;" + str(authorid) + '\n'
        f1.write(line)
f1.close()
    











