# CISC 121: Assignment 2
# Student Number: 10136014, Net ID:13aak15
# The following code was written by Alejandra Kudo

'''This function takes takes as an argument a filename
and returns a set containing all the words in the file.'''
def readStory(filename):
    f = set(open(filename).read().split())
    return f
    f.close()

'''This function takes two arguments, a set of words story
and a single word w. The word should return true if the word w
is part of the set story and false if not'''
def isInStory(story, w):
    if w in story:
           return True
    else:
           return False 

''' This function returns the 3x3 identity matrix.
A 3x3 matrix can be represented as a list of three rows'''
def identity3x3():
    return [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]

'''This function returns the transposed matrix of m**T of M.
It does not modify m but creates a new matrix.'''
# Using list comprehension to get a new transposed matrix 
def transpose3x3(m):
    mT = [list(i) for i in zip(*m)] 
    return mT

'''This function takes a filename as an argument, and
returns a dictionary containing the teams' players' batting averages.
The batting average is calculated using a formula provided by Professor Kunz'''
# using a for loop to iterate through each index by creating a list, the strip method
# then calculating the batting average and returning a dictionary 
def getTeamBattingAverageStats(filename):
    f = open(filename).read()
    d = {}
    for linestring in f:
        line = split.(',')
        batting_average = line[2]/line[1]
        d[line[0]] = batting_average
    return d 

'''This function takes a dictionary as an argument containing
the team batting average BA and returns the number of players
on the team which have a batting average of 0.25 or higher.'''
def numberOfTopHitters(teamBA):
    count = 0 
    for linestring in teamBA:
        batting_average = teamBA[linestring]
        if batting_average >= 0.25:
            count += 1
    return count 

'''This function takes a dictionary as an argument containing
the team batting average, BA, and returns the name of the player
with the highest batting average'''
def topBatter(teamBA):
    max = 0
    name = ''
    for linestring in teamBA:
        if teamBA[linestring] > max:
            max = teamBA[linestring]
            name = linestring
    return name 
