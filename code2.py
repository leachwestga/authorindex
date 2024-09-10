numberOfAuthors = 10
numberOfAuthors = 2092

def openauthor(number):
    authorfile = "authorfiles/file" + str(number) +".txt"
#    print(authorfile)
    f = open(authorfile, "r")
    
    name= f.readline().strip()
        
    papers = f.readlines()
    for i in range(len(papers)-1):
        papers[i]=papers[i].strip()
        papers[i]=papers[i][1:]
        papers[i]=papers[i].strip()
        if (papers[i][0]=="("):
            closingparen = papers[i].index(")") + 1
            papers[i]=papers[i][closingparen:]
            papers[i]=papers[i].strip()
#        print(papers[i])
    f.close()
    return([name,papers])

def getAuthorname(number):
    authorfile = "authorfiles/file" + str(number) +".txt"
#    print(authorfile)
    f = open(authorfile, "r")
    name= f.readline().strip()
    tries = 10
    while(len(name)==0 and tries > 0):
        name= f.readline().strip()
        tries = tries - 1
    name=name[5:]
    f.close()
    return(name)



##a = openauthor(16)
##
##print(a[0])
##for i in a[1]:
##    print(i)

class AuthorRecord:
    def __init__(self, ID, name):
        self.ID=ID
        self.name=name

    def __str__(self):
        return(str(self.ID) + " " + self.name)

    def toCsvLine(self):
        c = str(self.ID)
        c += ", "
        c += self.name
        c += '\n'
        return(c)
        
authorlist = []
count= 0
for i in range(1,numberOfAuthors):
    name = getAuthorname(i)
    print(name)
    if (len(name) > 1):
        authorlist.append(AuthorRecord(count,name))
        count=count+1

for i in authorlist:
    print(i.toCsvLine())

outfile = open("authorlist.csv","w")
for i in authorlist:
    print(i.toCsvLine())
    outfile.write(i.toCsvLine())
outfile.close()
