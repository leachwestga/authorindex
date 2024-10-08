import re
import os
from datetime import datetime
import sys

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
        return s;

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

class Authorship:
    def __init__(self, authorID, paperID):
        self.authorID = authorID
        self.paperID = paperID


# Read in the webpage (later change this to get it via an
#     http request)
#f = open("shortsite.html","r")
f = open("latest.html","r")
ijpage = f.read()
f.close

# split the html into the articles
articles = ijpage.split("<li class=fragment>")
volumeNumber = articles.pop(0) #remove the first element b/c it's not an article, but extract the volume number from ie
volumeNumber = volumeNumber.replace('\n',' ')
volumeNumber = re.sub(r".*Volume\s*", "", volumeNumber)
volumeNumber = re.sub(r"\s.*", "", volumeNumber)
#volumeNumber = int(volumeNumber)




# extract the titles
newtitles = []
for i in range(len(articles)):
    articles[i] = re.sub("errata.pdf.*</ul>","",articles[i].replace('\n',' '))
    articles[i] = re.sub("addendum.pdf.*</ul>","",articles[i].replace('\n',' '))
    articles[i] = re.sub(".*blank>","",articles[i].replace('\n',' '))
    newtitles.append(articles[i])
    newtitles[i] = re.sub("</a>.*","",newtitles[i]).strip()

# Read in the paperlist
existingPapers={}
f3 = open('uniquepaperlist.txt','r')
for line in f3:
    b = line.split(";;")
    print(b)
    existingPapers[int(b[0])]=Paper(b[0],b[1],b[2].strip());
f3.close()

prevmax=max(existingPapers.keys())
nextPaperID = max(existingPapers.keys()) + 1
newpapers={}
# check to see if the papers are already listed in uniquepaperlist.txt        
for i in newtitles:
    print(i[:60], end=" ")
##    paperIDNumber = 0;
##    print(i + "> ", end="")
    try:
        inospace = re.sub(r"[^A-Za-z0–9]","",i)
        paperIDNumber = list({ii for ii in existingPapers if re.sub(r"[^A-Za-z0–9]","",existingPapers[ii].title)==inospace})[0]
        print ("-->" + str(paperIDNumber))
    except:
        print("--> not found")
        existingPapers[nextPaperID]=Paper(nextPaperID, i, volumeNumber)
        newpapers[nextPaperID]=Paper(nextPaperID, i, volumeNumber)
        nextPaperID = nextPaperID + 1;


for i in range(prevmax,nextPaperID):
    print(existingPapers[i].todelimitedstring())

f=open("newpapers.txt", "w")
for i in newpapers.keys():
    f.write(newpapers[i].todelimitedstring())
f.close()





# if update is specified on command line, update the uniquepaperlist.txt file
if (len(sys.argv)>1):
    if (sys.argv[1]=="update"):
        now = datetime.today().strftime('%Y-%m-%d')
        backupfilename = "uniquepaperlist_" + str(now) + ".txt"
        os.system("cp uniquepaperlist.txt " + backupfilename)
        os.system("cat uniquepaperlist.txt newpapers.txt > a")
        os.system("mv a uniquepaperlist.txt")
    else:
        print("Argument " + sys.argv[1] + " not recognized.")



## REMAINING TO DO
## append the new papers to uniquepaperlist.txt        





