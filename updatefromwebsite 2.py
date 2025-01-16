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
    def __init__(self, ID, title, volume, authors):
        self.ID=ID
        self.title=title
        self.volume = volume
        self.authors=authors

    def addauthor(self,newauth):
        self.authors.append(newauth)

    def todelimitedstring(self):
        s  = self.ID + ";;"
        s += self.title + ";;"
        s += self.volume + ";;"

        for i in self.authors:
            s += str(i).strip() +" "
            print("====>" + s)
        return s

class Authorship:
    def __init__(self, authorID, paperID):
        self.authorID = authorID
        self.paperID = paperID

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
f = open("integerssite.html","r")
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
    articles[i] = re.sub(".*</a> </b>  <ul><li> ","",articles[i].replace('\n',' '))
    newnames.append(articles[i])
    newnames[i] = re.sub("<ul>.*","",newnames[i]).strip()

# Split the newnames string into a list of author strings
for i in range(len(newnames)):
    tmplist = []
    words = newnames[i].split(',')

    j=0;
    while j < len(words):
        words[j]=words[j].strip()
        print(j, end="")
        if j>0 and re.match("Jr.*|Sr.*", words[j]):
            print("FOUND:  ", end="")
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


# make a flat list of the authors of the new papers
authornames=[]
nextAuthorID = max(existingAuthors.keys())+1
for i in newnames:
    for j in i:
        authornames.append(lastnamefirst(j))
newAuthors = []
# check to see if the authors are already listed in authorindex.txt        
for i in authornames:
    theirIDNumber = 0;
    print(i + " ", end="")
    try:
        theirIDNumber=list(existingAuthors.keys())[list(existingAuthors.values()).index(i)]
        print ("-->" + str(theirIDNumber))
    except:
        print("not found")
        newAuthors.append(Author(nextAuthorID,i))
        nextAuthorID = nextAuthorID + 1;



   # if so, get the authorID
   # if not, assign a new AuthorID and add them to authorlist.txt

# Add the paper to uniquepaperlist.txt

# generate new author/paper pairs and add them to associationtable.txt

# regenerate the author index page


for i in newAuthors:
    print(i.todelimitedstring())

    

##
##for i in range(len(newtitles)):
###    print(str(i) + " " + newtitles[i])
##    print(str(i) + " "+str(newnames[i]))
##    print("-------------------------------")
##

        





