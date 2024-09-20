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

def authorpapers(aID):
    p = getPapersByAuthor(aID)
    print(authors[aID])
    for i in p:
        print("     " + papers[i].title + ", Vol " + papers[i].volume)

