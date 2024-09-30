import re



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
        return s

class Authorship:
    def __init__(self, authorID, paperID):
        self.authorID = authorID
        self.paperID = paperID


# Read in the webpage (later change this to get it via an
#     http request)
#f = open("shortsite.html","r")
f = open("integerssite.html","r")
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
    existingPapers[int(b[0])]=Paper(b[0],b[1],b[2].strip());
f3.close()

prevmax=max(existingPapers.keys())
nextPaperID = max(existingPapers.keys()) + 1

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
        nextPaperID = nextPaperID + 1;


for i in range(prevmax,nextPaperID):
    print(existingPapers[i].todelimitedstring())


## REMAINING TO DO
## append the new papers to uniquepaperlist.txt        





