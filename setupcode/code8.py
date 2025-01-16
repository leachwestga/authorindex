from unidecode import unidecode
import html
from html.parser import HTMLParser


class Authorship:
    def __init__(self, authorID, paperID):
        self.authorID = authorID
        self.paperID = paperID        

class Paper:
    def __init__(self, ID, title, volume):
        self.ID=ID
        self.title=title
        self.volume = volume



# Read in the association table
associations = []
f = open("associationtable.txt","r")
for line in f:
    b = line.split(";;")
    associations.append(Authorship(int(b[0]),int(b[1])))
f.close()


# Read in the authorlist
authors={}
f = open("authorlist.txt","r")
for line in f:
    b = line.split(";;")
    authors[int(b[0])]=b[1].strip()
f.close()


# Read in the paperlist
papers={}
f3 = open('uniquepaperlist.txt','r')
for line in f3:
    b = line.split(";;")
    papers[int(b[0])]=Paper(b[0],b[1],b[2].strip());
f3.close()


def firstnamefirst(input):
##    print(input)
    n = input.split(',')
    return n[1].strip() + " " + n[0].strip()


##for i in range(10):
##    print(str(associations[i].authorID) + " " + str(associations[i].paperID))


def getPapersByAuthor(author):
    plist = []
    for i in associations:
        if (i.authorID == author):
            plist.append(i.paperID)
    
    return plist

def getAuthorsOfPaper(paper):
    alist = []
    for i in associations:
        if (i.paperID == paper):
            alist.append(i.authorID)
    return alist

def getCoauthors(thisPaperID, thisAuthorID):
    coauthors=[]
    for i in associations:
        if (i.paperID == thisPaperID):
            if (i.authorID != thisAuthorID):
                coauthors.append(i.authorID)
    return coauthors  
                

def authorpapers(aID):
    p = getPapersByAuthor(aID)
    print(authors[aID])
    for i in p:
        print("     " + papers[i].title + ", Vol " + papers[i].volume)





def generateAuthorEntry(author):
    entry = ""
    entry += authors[author]
    entry += "\n"
    p = getPapersByAuthor(author)
    for pap in p:
        entry += "   " + papers[pap].title
        entry += ", Vol " + papers[pap].volume
        coau = getCoauthors(pap,author)
        if len(coau) > 0:
            entry += " (with "
            for i in coau:
                entry += firstnamefirst(authors[i]) + ", "
            entry = entry[:-2]
            entry +=")"
            
        entry +="\n"
    return entry

def generateWebAuthorEntry(author):
    entry = "<a name='"
    entry += str(author)
    entry += "'>"
    entry += "<li>"
    entry += authors[author]
    entry += "\n <ul>"
    p = getPapersByAuthor(author)
    for pap in p:
        entry += "<li>" + papers[pap].title
        entry += '<a href="vol'
        entry += papers[pap].volume
        entry += '">'
        entry += ", Vol " + papers[pap].volume
        entry += "</a>"
        coau = getCoauthors(pap,author)
        if len(coau) > 0:
            entry += " (with "
            for i in coau:
                entry +='<a href=#'
                entry += str(i)
                entry += '>'
                entry += firstnamefirst(authors[i]) + "</a>, "
            entry = entry[:-2]
            entry +=")"
        entry +="</li>"
    entry +="</ul></li>\n<br>\n"
    return entry

webpage = """
<html>
<head>
<title>
Author Index
</title>
  <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
    <script id="MathJax-script" async
          src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
  </script>
</head>
<body bgcolor="white" link="#0000B3" vlink="#0000B3" alink="white">
<style type="text/css">
a {text-decoration:none;}
</style>
<center>
<img src="smallbanner.gif">
<p>
<b><font size=+1>Author Index</font></b>
</center>
<ul>
"""

# create alphabetized list of authors
alphaAuthors=[]
h = html.parser
for i in authors:
#    alphaAuthors.append([authors[i].lower(),i])
    name=authors[i]
    name=h.unescape(name)
    name=unidecode(name)
    name=name.lower()
    alphaAuthors.append([name,i])


alphaAuthors.sort()



for i in alphaAuthors:
##    print(generateAuthorEntry(i))
    webpage+=generateWebAuthorEntry(i[1])







webpage += """</ul>
</font>
<p>
<hr>
<p>
</body>
</html>"""

f = open("out.html","w")
for i in webpage:
    f.write(i)
f.close()

