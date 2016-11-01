def findCubeDiffColour(listOfCubes, length, colour):
    for item in listOfCubes:
        if item[0] == length and item[1] != colour:
            return item

# cube format: (7, "blue")
def buildCubeTower(inputCubes, towerOfCubes = [], discardedCubes = [], duplicates = True, isSorted = False):
        if len(inputCubes) == 0:
            print(str(towerOfCubes))
            return () # is this required?
        # remove duplicates
        # sort

        # check whether the current cube is correctly placed
        ultCube = inputCubes[-1]
        penultCube = inputCube[-2]
        if ultCube[1] == penultCube[1]: # the last two cubes are of the same colour
            currentCubeSameSizeDiffColour = findCubeDiffColour(inputCubes, towerOfCubes[-1][0], towerOfCubes[-1][1])
            lowerCubeSameSizeDiffColour = findCubeDiffColour(inputCubes, towerOfCubes[-2][0], towerOfCubes[-2][1])
            if currentCubeSameSizeDiffColour is not None: # if there is a cube of the same size but of different colour to substitute the topmost coinciding one
                discardedCubes.append(towerOfCubes[-1]) # put current topmost cube in discarded
                del towerOfCubes[-1] # remove current topmost from tower
                towerOfCubes.append(currentCubeSameSizeDiffColour)
                inputCubes.remove(currentCubeSameSizeDiffColour) # remove currentCubeSameSizeDiffColour from inputCubes
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
                buildCubeTower(inputCubes, towerOfCubes, discardedCubes, True, False) # check the last two parameters

            else:
                pass


        # put next cube of smaller size
