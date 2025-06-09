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
re.sub("Start//-->", "Start //-->",ijpage)
re.sub("End//-->", "End //-->",ijpage)
f.close

# split the html into the articles
articles = ijpage.split("<!-- ArticleSectionStart //-->")
articles.pop(0) #remove the first element because it's header information, not an article
# extract the author names
authornames=[]

for i in range(len(articles)):
    print("=========================")
    # print(articles[i])
    # print("=========================")

    tmplist = articles[i].split("<!-- AuthorNameStart //-->")
    tmplist.pop(0) # remove first element b/c it's not a name
    for i in range(len(tmplist)):
        tmplist[i] = re.sub("<!-- AuthorNameEnd //-->.*","",tmplist[i].replace('\n',' '))
        tmplist[i] = re.sub(",\s*$","",tmplist[i])
        print(tmplist[i])
        authornames.append(lastnamefirst(tmplist[i]))


# remove duplicates
authornames = list(set(authornames))
print("AUTHORNAMES")
print(authornames)
print("++++++++++++++++++++++++++++++++++")
print("+                                +")
print("++++++++++++++++++++++++++++++++++")
newAuthors = []
nextAuthorID = max(existingAuthors.keys())+1

# Find authors who are not already in authorlist.txt
for i in authornames:
    theirIDNumber = 0;
    try:
        theirIDNumber=list(existingAuthors.keys())[list(existingAuthors.values()).index(i)]
        print("found " + i)
    except:
        newAuthors.append(Author(nextAuthorID,i))
        print("new: ", i)
        nextAuthorID = nextAuthorID + 1;


for i in newAuthors:
    print(i.todelimitedstring().strip())

# create a file containing new authors
f=open("newauthors.txt", "w")
for i in newAuthors:
    f.write(i.todelimitedstring())
f.close()



# if update is specified on command line, update the authorlist.txt file
if (len(sys.argv)>1):
    if (sys.argv[1]=="update"):
        now = datetime.today().strftime('%Y-%m-%d')
        backupfilename = "authorlist_" + str(now) + ".txt"  
        os.system("cp authorlist.txt " + backupfilename)
        os.system("cat authorlist.txt newauthors.txt > a")
        os.system("mv a authorlist.txt")
    else:
        print("Argument " + sys.argv[1] + " not recognized.")


        





