import re



class Author:
    def __init__(self, ID, name):
        self.ID=ID
        self.name=name

    def __str__(self):
        return(str(self.ID) + " " + self.name)

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



# Read in the webpage (later change this to get it via an
#     http request)
f = open("shortsite.html","r")
ijpage = f.read()
f.close

# split the html into the articles
articles = ijpage.split("<li class=fragment>")
articles.pop(0) #remove the first element because it's header information, not an article

# extract the titles
newtitles = []
for i in range(len(articles)):
    articles[i] = re.sub("errata.pdf.*</ul>","",articles[i].replace('\n',' '))
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
# Check to see if the authors already exist in the "database"
   # if so, get the authorID
   # if not, assign a new AuthorID and add them to authorlist.txt

# Add the paper to uniquepaperlist.txt

# generate new author/paper pairs and add them to associationtable.txt

# regenerate the author index page


for i in newtitles:
    print(i)
print()
for i in newnames:
    print(i)














