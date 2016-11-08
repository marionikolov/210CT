def findLongestIncreasingSubsequence(seq):
    longest = [0, 0] # start, length
    testLongest = [-1, 1]
    for i in range(0, len(seq) - 1):
        if testLongest[0] == -1:
            testLongest[0] = i
        if seq[i] < seq[i + 1]:
            testLongest[1] += 1
        else:
            if testLongest[1] > longest[1]:
                longest = testLongest
            testLongest = [-1, 1]
    return seq[longest[0]:longest[0] + longest[1]]

testList = [1,2,3,4,5,1,2,3,4,5,6,7,7,7,7,7,1,1,1,1,5,1,6,7,190,191,192,193,194,1]
answer = findLongestConsecutiveSubsequence(testList)
print(answer)