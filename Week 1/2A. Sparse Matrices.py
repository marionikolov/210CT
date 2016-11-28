class SparseMatrix:
    """
    Special class for sparse matrices. Instantiates a sparse matrix using two arguments:
    - a dictionary, whose keys as the coordinates of each number in the matrix and whose values are the numbers themselves;
    - a two-dimensional tuple containing the number of rows and columns of the matrix.
    Example: spMatrix = SparseMatrix({(1,1): 4, (1,3): 1, (2,2): 1}, (2, 3))
    """

    def __init__(self, value, dimensions):
        self.value = value
        self.dimensions = dimensions

    def __str__(self):
        return "SparseMatrix(%s, %s)" % (self.value, self.dimensions)

    def __add__(self, other):
        try:
            if isinstance(other, SparseMatrix):
                if self.dimensions != other.dimensions:
                    raise TypeError("Addition of sparse matrices with different dimensions is not defined.")
                else:
                    resultantMatrix = SparseMatrix({}, self.dimensions) # set the dimensions of the new matrix to the dimensions of the first one
                    for key in self.value: # iterate through all values in the first matrix
                        if key in other.value:
                            resultantMatrix.value[key] = self.value[key] + other.value[key]
                        elif key not in other.value:
                            resultantMatrix.value[key] = self.value[key]
                    for key in other.value:
                        if key in self.value:
                            pass # pass as we have already done the addition operation on these numbers
                        elif key not in self.value:
                            resultantMatrix.value[key] = other.value[key]
                    return resultantMatrix
            else:
                return NotImplemented
        except TypeError:
            print("A TypeError occurred.")
            raise

    def __sub__(self, other):
        try:
            if isinstance(other, SparseMatrix):
                if self.dimensions != other.dimensions:
                    raise TypeError("Addition of sparse matrices with different dimensions is not defined.")
                else:
                    resultantMatrix = SparseMatrix({}, self.dimensions) # set the dimensions of the new matrix to the dimensions of the first one
                    for key in self.value: # iterate through all values in the first matrix
                        if key in other.value:
                            resultantMatrix.value[key] = self.value[key] - other.value[key]
                        elif key not in other.value:
                            resultantMatrix.value[key] = -self.value[key]
                    for key in other.value:
                        if key in self.value:
                            pass # pass as we have already done the substraction operation on these numbers
                        elif key not in self.value:
                            resultantMatrix.value[key] = -other.value[key]
                    return resultantMatrix
            else:
                return NotImplemented
        except TypeError:
            print("A TypeError occurred.")
            raise

    def __mul__(self, other):
        try:
            if isinstance(other, SparseMatrix):
                if self.dimensions[1] != other.dimensions[0]:
                    raise TypeError("For matrix addition to be possible the number of columns of the first matrix must equal the number of rows of the second matrix.")
                else:
                    resultantMatrix = SparseMatrix({}, (self.dimensions[0], self.dimensions[1])) # set the number of rows in the resultant matrix as the number of rows of the first and the number of columns as the number of columns of the second
                    for j in range (1, self.dimensions[0] + 1): # iterate through the rows of the first matrix; j denotes the rows of the resultant matrix
                        for i in range(1,other.dimensions[1] + 1): # iterate through the columns of the second matrix; i denotes the columns of the resultant matrix
                            for k in range (1, self.dimensions[1] + 1): # iterate through the columns of the first matrix
                                if (j,k) in self.value and (k,i) in other.value: # only do multiplication if both numbers are non-zeros; our SparseMatrix class does not record zeros
                                    if (j,i) not in resultantMatrix.value:
                                        resultantMatrix.value[(j,i)] = 0
                                    resultantMatrix.value[(j, i)] += self.value[(j,k)]*other.value[(k,i)]
                    return resultantMatrix
            else:
                return NotImplemented
        except TypeError:
            print("A TypeError occurred.")
            raise

if __name__ == "__main__":
    sm1 = SparseMatrix({(2,2): 1, (3,1): 2}, (3,2))
    sm2 = SparseMatrix({(1,1): 1, (3,1): 3}, (3,2))
    sm3 = SparseMatrix({(1,1): 4, (1,3): 1, (2,2): 1}, (2,3))
    sm4 = SparseMatrix({(1,1): 1, (2,2): 2}, (3,2))

    sm12a = sm1 + sm2
    print(sm12a)
    sm12s = sm1 - sm2
    print(sm12s)
    sm34m = sm3 * sm4
    print(sm34m)