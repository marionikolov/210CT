def findFirstSmallerCube(listOfCubes, length):
    for item in listOfCubes:
        if item[0] < length:
            return item

def findCubeDiffColour(listOfCubes, length, colour):
    for item in listOfCubes:
        if item[0] == length and item[1] != colour:
            return item

# cube format: (7, "blue")
def buildCubeTower(inputCubes, towerOfCubes = [], discardedCubes = [], duplicates = True, isSorted = False):
    if len(inputCubes) == 0: # base case also needs to evaluate when there is no smaller cube to use
        print(str(towerOfCubes))
        print("Exited")
        return ()

    if duplicates:
        inputCubes = list(set(inputCubes))
        duplicates = False

    if not isSorted:
        inputCubes.sort(key = lambda x: x[0], reverse = True)
        isSorted = True

    # check whether the current cube is correctly placed
    if len(towerOfCubes) == 0:
        towerOfCubes.append(inputCubes[0])
        del inputCubes[0]
        print(str(towerOfCubes))
        buildCubeTower(inputCubes, towerOfCubes, discardedCubes, False, True)
    else:
        if len(towerOfCubes) >= 2:
            ultCube = towerOfCubes[-1]
            penultCube = towerOfCubes[-2]
            if ultCube[1] == penultCube[1]: # the last two cubes are of the same colour
                currentCubeSameSizeDiffColour = findCubeDiffColour(inputCubes, towerOfCubes[-1][0], towerOfCubes[-1][1])
                lowerCubeSameSizeDiffColour = findCubeDiffColour(inputCubes, towerOfCubes[-2][0], towerOfCubes[-2][1])
                if currentCubeSameSizeDiffColour is not None: # if there is a cube of the same size but of different colour to substitute the topmost coinciding one
                    discardedCubes.append(towerOfCubes[-1]) # put current topmost cube in discarded
                    del towerOfCubes[-1] # remove current topmost from tower
                    towerOfCubes.append(currentCubeSameSizeDiffColour)
                    inputCubes.remove(currentCubeSameSizeDiffColour) # remove currentCubeSameSizeDiffColour from inputCubes
                    print(str(towerOfCubes))
                    buildCubeTower(inputCubes, towerOfCubes, discardedCubes, False, True) # check the last two parameters
                elif lowerCubeSameSizeDiffColour is not None: # if there is a bigger cube of same size but diff colour to substitute the lower coinciding cube
                    currentCubeSize = towerOfCubes[-1][0] # get the size of the current topmost cube
                    inputCubes.append(towerOfCubes[-1]) # return the current topmost cube to the inputCubes list
                    del towerOfCubes[-1]
                    for cube in discardedCubes: # return all cubes of the same size as the now returned topmost cube to the inputCubes list
                        if cube[0] == currentCubeSize:
                            inputCubes.append(cube)
                    discardedCubes.append(towerOfCubes[-1])
                    del towerOfCubes[-1]
                    towerOfCubes.append(lowerCubeSameSizeDiffColour)
                    inputCubes.remove(currentCubeSameSizeDiffColour)
                    print(str(towerOfCubes))
                    buildCubeTower(inputCubes, towerOfCubes, discardedCubes, True, False) # check the last two parameters
        currentCubeSize = towerOfCubes[-1][0]
        nextCubeToPut = findFirstSmallerCube(inputCubes, currentCubeSize)
        if nextCubeToPut is None:
            buildCubeTower(inputCubes, towerOfCubes, discardedCubes, False, True)
        else:
            towerOfCubes.append(nextCubeToPut)
            inputCubes.remove(nextCubeToPut)
            print(str(towerOfCubes))
            buildCubeTower(inputCubes, towerOfCubes, discardedCubes, False, True) # check the last two parameters

if __name__ == "__main__":
    data = [(2, 'red'), (1, 'purple'), (4, 'blue'), (2, "purple")]
    buildCubeTower(data)