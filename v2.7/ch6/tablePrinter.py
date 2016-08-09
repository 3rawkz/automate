tableData = [['apples', 'oranges', 'cherry', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def findLongest(dataList):
    longest = 0
    for i in dataList:
        if longest < len(i):
            longest = len(i)
    return longest

def findLargest(tData):
    large = 0
    for i in tData:
        if large < len(i):
            large = len(i)
    return large

def printTable(tData):
    colWidth = [0] * len(tData)
    for i in range(len(colWidth)):
        colWidth[i] += findLongest(tData[i])

    size = findLargest(tData)
    for i in range(size):
        for j in range(len(colWidth)):
            print tData[j][i].rjust(colWidth[j]),
        print '\n'

printTable(tableData)
