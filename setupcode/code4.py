
import csv
import sys


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


# read in the list of authors
file = open('authorlist.csv')
reader = csv.reader(file)
authorlist=[]

for line in reader:
    print(line)
    name = ""
    id = int(line[0])
    name = line[1].strip()
    if (len(line)>2):
        name += ", " + line[2].strip()
    if (len(line)>3):
        name += ", " + line[3].strip()
    authorlist.append(Author(id, name))
file.close()

authorlist.sort(key=lambda x: x.name)
for i in authorlist:
    print(i)

#read in the unique list of papers
uniquepaperlist={}
f2 = open('uniquepaperlist.csv')
for line in f2:
    b = line.split(";;")
    print(line)
    uniquepaperlist[int(b[0])] = Paper(b[0],b[1],b[2].strip(),[])
f2.close()

# read in the list of all papers with author ids
# and generate a list of author-paper pairs

llist = []
f3 = open('paperlist.txt','r')
for line in f3:
    b = line.split(";;")
    print(line)
    llist.append([b[0],b[2]])
f3.close()

def findbytitle(t):
    returnval = -1
    for i in uniquepaperlist.keys():
##        print("--->" + uniquepaperlist[i].title)
        if(str(uniquepaperlist[i].title)==str(t)):
            returnval = uniquepaperlist[i]
    return returnval
                
##gg = findbytitle("A Note on Incomplete Leonardo Numbers")
##uniquepaperlist[gg]
##uniquepaperlist[gg].addauthor(123)
##print(gg)
##print(uniquepaperlist[gg].todelimitedstring())

gg = findbytitle("A Note on Incomplete Leonardo Numbers")
gg.addauthor(123)
print(gg)


print("Now")
for i in llist:
    t = findbytitle(i[0])
    if (t != -1):
        t.addauthor(i[1])
        print(t.todelimitedstring())



outfile = open("newfile.txt","w")

for i in uniquepaperlist.keys():
    outfile.write(uniquepaperlist[i].todelimitedstring())
    outfile.write('\n')
outfile.close()










