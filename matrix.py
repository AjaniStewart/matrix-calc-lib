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
            sumMatrix = [[self.matrix[row][col]+other.matrix[row][col] 
                        for col in range(self.cols)] 
                        for row in range(self.rows)]
            return Matrix(sumMatrix)

    def __rmul__(self, other):
        if (not(hasattr(other, "__iter__"))): # scalar product
            productMatrix = [[other*x for x in self.matrix[i]] for i in range(self.rows)]
            return Matrix(productMatrix)

    def __mul__(self, other):
        if isinstance(other,Matrix): # matrix mulitplication
            if self.cols != other.rows:
                raise MatrixError("Dimension mismatch")
            else:
                # iterate over the cols of self and rows of other
                result = [
                    [sum([self.matrix[row][i]*other.matrix[i][col] for i in range(self.cols)])
                    for col in range(other.cols)] for row in range(self.rows)]
                return Matrix(result)
        else:
            return other * self #scalar product
    
    def transpose(self):
        result = [[self.matrix[i][j] for i in range(self.rows)] for j in range(self.cols)]
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
    matrix = [[int(col) for col in row.split(',')] for row in inString.split(";")]
    return matrix


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
    # matrixE = Matrix([[2],[3]])
    #(matrixB + matrixE).read()
    # matrixA.read()
    # matrixB.read()
    # matrixA.read()
    # matrixA.transpose().read()
    matrixC.read()
    matrixD.read()
    (matrixC + matrixD).read()
    matrixD.transpose().read()
    matrixE = Matrix(stringToList("1,0,0;0,1,0;0,0,1"))
    matrixE.read()
    #matrixD.read()
