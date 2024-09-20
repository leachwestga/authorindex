# 
# generate an association list from
# the authorlist and paperlist
# 
# 

class Authorship:
    def __init__(self, authorID, paperID):
        self.authorID = authorID
        self.paperID = paperID        

class Paper:
    def __init__(self, ID, title, volume):
        self.ID=ID
        self.title=title
        self.volume = volume

associations = []

f = open("assocList.txt","r")
for line in f:
    b = line.split(";;")
    authors = b[1].split()
    for i in authors:
        associations.append(Authorship(i,b[0]))
f.close()

f3 = open("h.txt","w")
for i in associations:
    print(i.authorID + ";;" + i.paperID)
    f3.write(i.authorID + ";;" + i.paperID+"\n")
f3.close()

