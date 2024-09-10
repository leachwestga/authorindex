numberOfAuthors = 2120
numberOfAuthors = 25

def openauthor(number):
    authorfile = "author" + str(number)
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
    authorfile = "author" + str(number)
#    print(authorfile)
    f = open(authorfile, "r")
    name= f.readline().strip()
    f.close()
    return(name)


def testcode():
    for i in range(1,numberOfAuthors):
        name= getAuthorname(i)
        if (len(name) > 1):
            print(name + " " + str(hash(name))) 
    

##a = openauthor(16)

##print(a[0])
##for i in a[1]:
##    print(i)
##
##for i in range(1,10):
##    a = getAuthorname(i)
##    print(a)

