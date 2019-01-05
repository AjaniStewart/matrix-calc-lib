class MatrixError(Exception):
    def __init__(self,message):
        self.message = message


class Matrix(object):
    def __init__(self, matrixList):
        self.matrix = matrixList
        self.rows = len(self.matrix)
        self.cols = len(self.matrix[0])

    def __add__(self, other):
        if (not(isinstance(other, Matrix))):
            raise MatrixError("One addend is not a matrix")
        elif (self.rows!=other.rows or self.cols != other.cols):
            raise MatrixError("Dimension Mismatch")
        else:
            sumMatrix = []
            for row in range(self.rows):
                rowsum = []
                for col in range(self.cols):
                    rowsum.append(self.matrix[row][col]+other.matrix[row][col])
                sumMatrix.append(rowsum)
            return Matrix(sumMatrix)

    def __rmul__(self, other):
        if (not(hasattr(other, "__iter__"))): # scalar product
            productMatrix = []; scalar = other
            for row in range(self.rows):
                colproducts = []
                for col in range(self.cols):
                    colproducts.append(scalar * self.matrix[row][col])
                productMatrix.append(colproducts)
            return Matrix(productMatrix)

    def __mul__(self, other):
        if isinstance(other,Matrix):
            if self.cols != other.rows:
                raise MatrixError("Dimension mismatch")
            else: # matrix mulitplication
                #create 'empty' 2d matrix
                result = Matrix([[None for _ in range(other.cols)] for _ in range(self.rows)])
                # iterate over the cols of self and rows of other
                for current_row in range(self.rows):
                    for current_col in range(other.cols):
                        sum = 0
                        for i in range(self.cols):
                            sum += self.matrix[current_row][i] * other.matrix[i][current_col]
                        result.matrix[current_row][current_col] = sum
            return result
        else:
            return other * self #scalar product
    
    def transpose(self):
        result = [[None for _ in range(self.rows)] for _ in range(self.cols)]
        for i in range(self.rows):
            for j in range(self.cols):
                result[j][i] = self.matrix[i][j]
        return Matrix(result)
        
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

# what is the point of having this here if read() does the same thing
def printMatrix(matrix):
    outString = ""
    for row in range(len(matrix)):
        outString += "|"
        for col in range(len(matrix[0])):
            outString += str(matrix[row][col]) + " "
        outString = outString[:-1]+"|\n"
    print(outString)

#removed error matrix

if __name__ == "__main__":
    # -- Rudementary Tests -- #

    # Input matrix with commas separating elements and semicolons terminating lines
    # inString = "1,0;0,1"
    # matrix = stringToList(inString)
    # identityMatrix2 = Matrix(matrix)

    # matrixA = Matrix(stringToList("1,0,0;0,1,0;0,0,1"))
    # matrixB = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])

    # matrixZ = Matrix(stringToList("1,0;0,1;0,1"))

    # printMatrix((matrixA + 5).matrix) # scalar error
    # printMatrix((matrixA + matrixZ).matrix) # cols wrong error
    # printMatrix((matrixA + identityMatrix2).matrix) # rows wrong error
    # printMatrix((matrixA + matrixB).matrix)

    # matrixC = 5 * matrixA
    # printMatrix(matrixC.matrix)
    # matrixD =  matrixC * 5
    # printMatrix(matrixD.matrix)

    # print(matrixD.toString())
    # matrixD.read()

    matrixA = Matrix([[5,3],[2,9],[-3,7],[18,4]])
    matrixB = Matrix([[9],[-3]])
    matrixC = matrixA * matrixB
    matrixD = matrixC * 5
    matrixE = Matrix([[2],[3]])
    #(matrixB + matrixE).read()
    # matrixA.read()
    # matrixB.read()
    matrixA.read()
    matrixA.transpose().read()
    #matrixD.read()
