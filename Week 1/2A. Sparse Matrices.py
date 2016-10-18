class SparseMatrix:
    """
    Special class for sparse matrices. Instantiate a sparse matrix using two arguments:
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

m1 = {(2,2): 1, (3,1): 2}
m2 = {(1,1): 1, (3,1): 3}

m1a = {(1,1): 4, (1,3): 1, (2,2): 1}
m2a = {(1,1): 1, (2,2): 2}
m1aDim = (2, 3)
m2aDim = (3, 2)

def addMatrices(m1, m2):
    m3 = {}
    for key in m1:
        if key in m2:
            m3[key] = m1[key] + m2[key]
        elif key not in m2:
            m3[key] = m1[key]
    for key in m2:
        if key in m1:
            pass
        elif key not in m1:
            m3[key] = m2[key]
    return m3

def substractMatrices(m1, m2):
    m3 = {}
    for key in m1:
        if key in m2:
            m3[key] = m1[key] - m2[key]
        elif key not in m2:
            m3[key] = -m1[key]
    for key in m2:
        if key in m1:
            pass
        elif key not in m1:
            m3[key] = -m2[key]
    return m3

def multiplyMatrices(m1a, m2a, m1aDim, m2aDim):
    if m1aDim[1] != m2aDim[0]:
        print("Error. Cannot multiply due to...")
    else:
        m3a = {}
        for j in range (1, m1aDim[0] + 1): # 2 rows in first matrix = rows in new matrix
            for i in range(1,m2aDim[1] + 1): # 2 cols in second matrix = cols in new matrix
                for k in range (1, m1aDim[1] + 1): # 3 cols in first matrix
                    if (j,k) in m1a and (k,i) in m2a:
                        if (j,i) not in m3a:
                            m3a[(j,i)] = 0
                        m3a[(j, i)] += m1a[(j,k)]*m2a[(k,i)]
        return m3a

m3 = addMatrices(m1, m2)
m4 = substractMatrices(m1, m2)
print(m3)
print(m4)

m5 = multiplyMatrices(m1a, m2a, m1aDim, m2aDim)
print(m5)

print("class test")

sm1 = SparseMatrix(m1, (3,2))
sm2 = SparseMatrix(m2, (3,2))
sm12 = sm1 - sm2
print (sm12)

sm3 = SparseMatrix(m1a, m1aDim)
sm4 = SparseMatrix(m2a, m2aDim)
sm34 = sm3 * sm4
print(sm34)