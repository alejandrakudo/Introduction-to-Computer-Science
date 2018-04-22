def readFile(filename):
## reads the file with songs and stores them into a list
## each song is a tuple (name, duration, release year)
    
    myList = list()   # init list
    
    try:
        ein = open(filename, 'r')
        ## read lines in file
        for l in ein.readlines():
            l.strip()     # remove EOL character
            l_list = l.split(',')   # separate items into list   
            t = l_list[0], int(l_list[1]), int(l_list[2])
            myList.append(t)

        ein.close()
        
    except FileNotFoundError:
        print("File", filename, "not found!")

    return myList

def printList(aList):
## prints the song list
## each line: one song
    for i in range(len(aList)):
        print(aList[i][0], aList[i][1], aList[i][2])
