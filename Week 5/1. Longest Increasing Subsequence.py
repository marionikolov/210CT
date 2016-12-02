"""
Returns the longest subsequence which is in ascending order from the input list seq.
PARAMETERS
    seq - list of numbers
"""
def findLongestIncreasingSubsequence(seq):
    longest = [0, 0] # variable which holds information on the longest subsequence in the format: [start index of the longest subsequence, length of the subsequence]
    testLongest = [-1, 1] # variable which holds information on the currently tested subsequence in the same format as above; first value initiated as -1 to show a test is to be run
    for i in range(0, len(seq) - 1):
        if testLongest[0] == -1:
            testLongest[0] = i
        if seq[i] < seq[i + 1]:
            testLongest[1] += 1
        else:
            if testLongest[1] > longest[1]:
                longest = testLongest # set the longest subsequence as the currently tested subsequence
            testLongest = [-1, 1] # reinitiate variable to repeat test
    return seq[longest[0]:longest[0] + longest[1]]

if __name__ == '__main__':
    testList = [1,2,3,4,5,1,2,3,4,5,6,7,7,7,7,7,1,1,1,1,5,1,6,7,190,191,192,193,194,1]
    answer = findLongestIncreasingSubsequence(testList)
    print(answer)