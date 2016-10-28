'''
    Returns the solution of a linear function in the form a*x + b = 0
    PARAMETERS
        x, a, b - integers or floating-point numbers
'''
def f(x, a, b):
    return a*x + b

'''
    Detects whether the change between the last two results of the functions is decreasing. Returns True if the change is decreasing and False if it is increasing.
    PARAMETERS
        penultX, penultY, ultX, ultY - integers
'''
def detectChange(penultX, penultY, ultX, ultY):
    return (penultX - penultY) > (ultX - ultY)
'''
    Returns the critical value of two linear functions a*x + b, i.e. the point at which the two plots of the two functions cross each other (in other words where f(x) = g(x)).
    The functions are defined by the user input for the multipliers and the constants.
    findCriticalValue() uses an iteritive approach to test for the critical value. It does so by testing the change of the difference of results the functions yield, i.e. f(x) - g(x). It assumes that the change is decreasing by default. Firstly, it tests whether the critical value is 0. If it is not, it then begins testing exponents of 10, which is called the testValue, and decreases the testValue when it detects that the change has begun increasing. It initaites the test with the new testValue beginning at the last result where the change was decreasing.
    N.B. This process is repeated until it finds the critical value. The algorithm can only detect critical values which are integers!
    PARAMETERS
        a, b, c, d - integers or floating-point numbers
    VARIABLES
        resultsF, resultsG - lists which hold the results of the two functions f(x) and g(x) respectively
        interval - the test interval; defaults to 10 and decreases gradually until the critical value is discovered
        initialTestValue - the value at which the testing should begin; defaults to 0; changes when an increase in the change of the difference of results the functions yield is detected; changes to the last testValue at which the change was decreasing
        exponent - the exponent applied to the testValue
        checkedForZero - determines whether findCriticalValue() has checked whether 0 is the critical value
        testValue - the current value we are applying for x in the two functions; determined by the current interval we are testing and the exponent applied to it; it's first value is always 0
'''
def findCriticalValue(a, b, c, d):
    resultsF = []
    resultsG = []
    interval = 10
    initialTestValue = 0
    exponent = 0
    checkedForZero = False
    while True:
        if not checkedForZero: # check whether the critical value is zero before testing other numbers
            testValue = 0
            checkedForZero = True
        else:
            testValue = interval**exponent
        x = f(initialTestValue + testValue, a, b)
        resultsF.append(x)
        y = f(initialTestValue + testValue, c, d)
        resultsG.append(y)

        print("=== NEW TEST ===")
        print("initialTestValue: " + str(initialTestValue))
        print("testValue: " + str(testValue))
        print("f(x): " + str(x))
        print("g(x): " + str(y))

        isDecreasing = True # assume the difference between the values of the two functions is decreasing
        numberOfResults = len(resultsF)
        if x == y: # test whether the current testValue is the critical value
            print("=== END TESTING ===")
            print("Critical value: " + str(initialTestValue + testValue))
            break
        else:
            if numberOfResults >= 2: # only start detecting of a change when we have sufficient results to test against
                currentChange = detectChange(resultsF[numberOfResults-2], resultsG[numberOfResults-2], resultsF[numberOfResults-1], resultsG[numberOfResults-1])
                print("current change: " + str(currentChange))
                if currentChange == isDecreasing: # continue testing with the same interval
                    pass
                else: # decrease test interval and set the initialTestValue to the last value at which the change was decreasing
                    # Clear results lists to avoid confusion with previous test values
                    resultsF = []
                    resultsG = []
                    if exponent > 1:
                        initialTestValue = interval**(exponent-1)
                    else:
                        initialTestValue = interval
                    interval -= 1
                    exponent = 0
                    continue
        exponent += 1

findCriticalValue(4,1,2,19)
