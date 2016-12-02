BINARY-SEARCH-WITHIN-RANGE(lst, x, y) // O(logn)
    firstLoc <- 0
    lastLoc <- length(lst) - 1
    WHILE lastLoc >= firstLoc
        testLoc = firstLoc + (lastLoc - firstLoc)//2
        IF lst[testLoc] >= x AND lst[testLoc] <= y
            RETURN TRUE
        ELSE IF lst[testLoc] < x
            firstLoc = testLoc + 1
        ELSE
            lastLoc = testLoc - 1
    RETURN FALSE