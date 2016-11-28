def isSorted(lst):
    for i in range(len(lst)-2):
        if lst[i] > lst[i+1]:
            return False
    return True

def binarySearchWithinRange(lst, x, y):
    if isSorted(lst) != True:
        lst.sort()
    firstLoc = 0
    lastLoc = len(lst) - 1
    while lastLoc >= firstLoc:
        testLoc = firstLoc + (lastLoc - firstLoc)//2
        if lst[testLoc] >= x and lst[testLoc] <= y:
            return True
        elif lst[testLoc] < x:
            firstLoc = testLoc + 1
        else:
            lastLoc = testLoc - 1
    return False

a = [2,3,4,7,9,13]
result = binarySearchWithinRange(a, 10, 14)
print(result)