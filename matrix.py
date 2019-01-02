class Matrix_(object):
    def __init__(self, matrixList):
        self.matrix = matrixList
        self.rows = len(self.matrix)
        self.cols = len(self.matrix[0])
    def __add__(self, other):
        if (not(hasattr(other.matrix, "__iter__"))):
            print("Error: One addend is not a matrix")
        elif (self.rows!=other.rows):
            print("Undefined Sum: number of rows differ")
            return errorMatrix(self.matrix)
        elif (self.cols!=other.cols):
            print("Undefined Sum: number of columns differ")
            return errorMatrix(matriself.matrix)
        else:
            sumMatrix = []
            for row in range(self.rows):
                rowsum = []
                for col in range(self.cols):
                    rowsum.append(self.matrix[row][col]+other.matrix[row][col])
                sumMatrix.append(rowsum)
            return Matrix_(sumMatrix)
    def __rmul__(self, other):
        if (not(hasattr(other, "__iter__"))): # scalar product
            productMatrix = []; scalar = other
            for row in range(self.rows):
                colproducts = []
                for col in range(self.cols):
                    colproducts.append(scalar * self.matrix[row][col])
                productMatrix.append(colproducts)
            return Matrix_(productMatrix)
    def __mul__(self, other):
        return other * self
    def toString(self):
        outString = ""
        for row in range(self.rows):
            outString += "|"
            for col in range(self.cols):
                outString += str(self.matrix[row][col]) + " "
            outString = outString[:-1]+"|\n"
        return (outString)
    def read(self):
        print(self.toString())

def stringToList(inString):
    if (inString[-1]==";"):
        # strip trailing semicolon if present
        inString = inString[:-1]
    rows = inString.split(";")
    matrix = []
    for row in rows:
        cols = row.split(',')
        colsList = []
        for col in cols:
            colsList.append(int(col))
        matrix.append(colsList)
    return matrix

def printMatrix(matrix):
    outString = ""
    for row in range(len(matrix)):
        outString += "|"
        for col in range(len(matrix[0])):
            outString += str(matrix[row][col]) + " "
        outString = outString[:-1]+"|\n"
    print(outString)

def errorMatrix(matrix1):
        undefOutList = []
        row, col = 0,0
        for row in range(len(matrix1)):
            rowlist = []
            for col in range(len(matrix1[0])):
                rowlist.append("*")
            undefOutList.append(rowlist)
        return undefOutList

#inString = input("Input matrix with commas separating elements and semicolons terminating lines")
inString = "1,0;0,1"
matrix = stringToList(inString)
identityMatrix2 = Matrix_(matrix)

matrixA = Matrix_(stringToList("1,0,0;0,1,0;0,0,1"))
matrixB = Matrix_([[1, 0, 0], [0, 1, 0], [0, 0, 1]])

printMatrix(matrixA + identityMatrix2)
printMatrix((matrixA + matrixB).matrix)

matrixC = 5 * matrixA
printMatrix(matrixC.matrix)
matrixD =  matrixC * 5
printMatrix(matrixD.matrix)

print(matrixD.toString())
matrixD.read()