import re
import os
from datetime import datetime
import sys

class Paper:
    def __init__(self, ID, title, volume):
        self.ID=ID
        self.title=title
        self.volume = volume

    def addauthor(self,newauth):
        self.authors.append(newauth)

    def todelimitedstring(self):
        s  = str(self.ID) + ";;"
        s += self.title + ";;"
        s += self.volume
        s += '\n'
        return s

class Author:
    def __init__(self, ID, name):
        self.ID=ID
        self.name=name

    def __str__(self):
        return(str(self.ID) + " " + self.name)

    def todelimitedstring(self):
        s  = str(self.ID)
        s += ";;"
        s += self.name;
        s += '\n'
        return s;

def lastnamefirst(n):
    words = n.split()
##    print(words)
    
    if len(words) == 1:
        return words[0]
    if len(words) == 2:
        return words[1] + ", " + words[0]
    hasDe = False
    deLocation = 0
    for i in range(len(words)):
#        print("testing " + words[i])
        if re.match("^de$|^El$|^el$|^De$|^dos$|^Di$|^di$|^van$|^von$|^Van$|^Von$|^Das$|^das$|^da$|^Da$|^te$", words[i]):
            deLocation = i
            hasDe = True
            break
    if hasDe:       
        lastfirst=""
 #       print("XXXXXXXXXXXXXX")
        for j in range(deLocation, len(words)):
            lastfirst += words[j]+ " "
        lastfirst = lastfirst[:-1]
        lastfirst += ", "
        for j in range(deLocation):
            lastfirst += words[j] + " "
        lastfirst = lastfirst[:-1]
        return lastfirst
    else:
        lastfirst = words[-1] + ", "
        for j in range(len(words)-1):
            lastfirst += words[j] + " "
        lastfirst=lastfirst[:-1]
        return lastfirst
    return -1




# Read in the authorlist.txt
existingAuthors={}
f = open("authorlist.txt","r")
for line in f:
    b = line.split(";;")
    existingAuthors[int(b[0])]=b[1].strip()
f.close()


# Read in the webpage (later change this to get it via an
#     http request)
#f = open("shortsite.html","r")
f = open("latest.html","r")
ijpage = f.read()
f.close

# split the html into the articles
articles = ijpage.split("<li class=fragment>")
articles.pop(0) #remove the first element because it's header information, not an article

# extract the titles
newtitles = []
for i in range(len(articles)):
   articles[i] = re.sub("errata.pdf.*</ul>","",articles[i].replace('\n',' '))
   articles[i] = re.sub("addendum.pdf.*</ul>","",articles[i].replace('\n',' '))
   articles[i] = re.sub(".*blank>","",articles[i].replace('\n',' '))
   newtitles.append(articles[i])
   
   newtitles[i] = re.sub("</a>.*","",newtitles[i]).strip()


# extract the author names
newnames = []
for i in range(len(articles)):
    articles[i] = re.sub(".*</a> </b>\s*<ul><li> ","",articles[i].replace('\n',' '))
    newnames.append(articles[i])
    newnames[i] = re.sub("<ul>.*","",newnames[i]).strip()

# Split the newnames string into a list of author strings
for i in range(len(newnames)):
    tmplist = []
    words = newnames[i].split(',')

    j=0;
    while j < len(words):
        words[j]=words[j].strip()
        # print(j, end="")
        if j>0 and re.match("Jr.*|Sr.*", words[j]):
            # print("FOUND:  ", end="")
##            print(words)
            words[j-1] = words[j-1] + " " + words[j]
            words.pop(j)
        j=j+1
    
    for j in words:
        j = j.strip()
        j = re.sub("^and ","",j)    
        if re.search(" and ",j):
            h = j.split(" and ")
            tmplist.append(h[0])
            tmplist.append(h[1])
        else:
            tmplist.append(j)
    newnames[i]=tmplist

existingPapers={}
f3 = open('uniquepaperlist.txt','r')
for line in f3:
    b = line.split(";;")
    existingPapers[int(b[0])]=Paper(b[0],b[1],b[2].strip());
f3.close()

IDnums = []
for i in newtitles:
    print(i[:60], end=" ")
##    paperIDNumber = 0;
##    print(i + "> ", end="")
    try:
        inospace = re.sub(r"[^A-Za-z0–9]","",i)
        paperIDNumber = list({ii for ii in existingPapers if re.sub(r"[^A-Za-z0–9]","",existingPapers[ii].title)==inospace})[0]
        IDnums.append(paperIDNumber)
        print ("-->" + str(paperIDNumber))
    except:
        print("--> not found")

newassociations = []
for i in range(len(newnames)):
        for j in newnames[i]:
            try:
                theirIDNumber=list(existingAuthors.keys())[list(existingAuthors.values()).index(lastnamefirst(j))]
#                print ("-->" + str(theirIDNumber))
                print(newtitles[i][:50], theirIDNumber, IDnums[i])
                newassociations.append([theirIDNumber, IDnums[i]])
            except:
                print(newtitles[i][:50], " not found ", IDnums[i])


f3 = open("newassociations.txt", "w")

for i in newassociations:
    f3.write(str(i[0]) + ";;" + str(i[1]) + '\n')
f3.close()


# if update is specified on command line, update the uniquepaperlist.txt file
if (len(sys.argv)>1):
    if (sys.argv[1]=="update"):
        now = datetime.today().strftime('%Y-%m-%d')
        backupfilename = "associationtable_" + str(now) + ".txt"
        os.system("cp associationtable.txt " + backupfilename)
        os.system("cat associationtable.txt newassociations.txt > a")
        os.system("mv a associationtable.txt")
    else:
        print("Argument " + sys.argv[1] + " not recognized.")

##
##for i in range(len(newtitles)):
###    print(str(i) + " " + newtitles[i])
##    print(str(i) + " "+str(newnames[i]))
##    print("-------------------------------")
##

        





