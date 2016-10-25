def f(x, a, b):
    return a*x + b

''' Returns True if change is decreasing '''
def detectChange(penultX, penultY, ultX, ultY):
    return (penultX - penultY) > (ultX - ultY)

def findCriticalValue(a, b, c, d):
    resultsX = []
    resultsY = []
    # run it on first
    # run on second
    # after two runs, detect mode - increasing/decreasing
    # after each consecutive run, check whether it has flipped
    # if flipped, detect number before flip and decrease interval of checking
    # clear results and start over NO!
    # continue checking and repeat
    interval = 10
    initialTestValue = 0
    exponent = 0
    while True:
        testValue = interval**exponent
        x = f(initialTestValue + testValue, a, b)
        resultsX.append(x)
        y = f(initialTestValue + testValue, c, d)
        resultsY.append(y)

        print("initial test value: " + str(initialTestValue))
        print("testValue: " + str(testValue))
        print("x: " + str(x))
        print("y: " + str(y))
        # add check for 0 !!!!

        isDecreasing = True # assume the difference between the values of the two functions is decreasing
        # detect growth
        numberOfResults = len(resultsX)
        if x == y:
            print("Critical value: " + str(initialTestValue + testValue))
            break
        else:
            if numberOfResults >= 2:
                currentChange = detectChange(resultsX[numberOfResults-2], resultsY[numberOfResults-2], resultsX[numberOfResults-1], resultsY[numberOfResults-1])
                print("current change: " + str(currentChange))
                if currentChange == isDecreasing:
                    pass
                else:
                    #del resultsX[-1]
                    #del resultsY[-1]
                    resultsX = []
                    resultsY = []
                    initialTestValue = interval**(exponent-1)
                    interval -= 1
                    exponent = 0
                    continue
        exponent += 1


findCriticalValue(4,1,2,19)
