class Matrix():

    def __init__(self, rows = False, columns = False, matrix = False):
        if(rows and columns):
            self.rows = rows
            self.cols = columns
            self.mat = []
            for i in range(0,self.cols-1):
                self.mat.append([])
                for  j in range(0,self.rows-1):
                    self.mat[i].append(0)
        elif(matrix):
            self.mat = matrix
            self.rows = len(matrix[0])
            self.cols = len(matrix)

    def multiplication(A, B):
        if(self.cols != self.rows):
            raise ValueError("Matrix multiplication: Columns != Rows")
        new = Matrix(self.rows, other.cols)
        for i in range(0,self.rows-1):
            for j in range(0,other.cols-1):
                for k in range(0,self.cols-1):
                    new.mat[i][j] += self.mat[k][i]*other.mat[j][k]
        return new

    def __mul__(self,other):
        return multiplication(A,B)

    def __add__(self,other):

        
        
