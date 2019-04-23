import code

class Matrix():

    def __init__(self, rows = False, columns = False, matrix = False):
        if(rows and columns):
            self.rows = rows
            self.cols = columns
            self.mat = []
            for i in range(0,self.cols):
                self.mat.append([])
                for  j in range(0,self.rows):
                    self.mat[i].append(0)
        elif(matrix):
            self.mat = matrix
            self.rows = len(matrix[0])
            self.cols = len(matrix)

    def matmul(self, other):
        if(self.cols != self.rows):
            raise ValueError("Matrix multiplication: Columns != Rows")
        new = Matrix(rows=self.rows, columns = other.cols)
        for i in range(0,self.cols):
            for j in range(0,other.rows):
                for k in range(0,self.cols):
                    new.mat[i][j] += self.mat[i][k]*other.mat[k][j]
        return new
    
    def scalmul(self,other):
        new = Matrix(rows=self.rows,columns=self.cols)
        for i in range(0,self.cols):
            for j in range(0,self.rows):
                new.mat[i][j] = self.mat[i][j] * other
        return new

    def trace(self):
        if(self.rows != self.cols):
            raise ValueError("Trace can only be done on square matrix")

        sum = 0
        for i in range(0,self.rows-1):
            sum += self.mat[i][i]
        return sum

    #Elementary row operations following:
    def elementarySwap(self,row1, row2):
        row1 -= 1
        row2 -= 1
        for i in range(0,self.cols):
            tmp = self.mat[row1][i]
            self.mat[row1][i] = self.mat[row2][i]
            self.mat[row2][i] = tmp
    
    def elementaryMul(self, row, scal):
        row -= 1
        for i in range(0,self.cols):
            self.mat[row][i] *= scal
    
    def elementaryAdd(self, row1, scal, row2):
        row1 -= 1
        row2 -= 1
        for i in range(0,self.cols):
            self.mat[row2][i] += self.mat[row1][i] * scal

    
    def rowreduce(self):
        pass


    def __mul__(self,other):
        if type(other) == type(1):
            return self.scalmul(other)
        else:
            return self.matmul(other)
    
    def __imul__(self,other):
        if type(other) == type(1):
            raise ValueError("Has to be a matrix")
        else:
            new = self.matmul(other)
            self.cols = new.cols
            self.rows = new.rows
            self.mat = new.mat

    def __add__(self,other):
        if self.rows != other.rows and self.cols != other.cols:
            raise ValueError("Matrixes has to be of same size for addition")
        new = Matrix(rows = self.rows, columns = self.cols)
        for i in range(0,self.cols):
            for j in range(0,self.rows):
                new.mat[i][j] = self.mat[i][j] + other.mat[i][j]
        return new
    
    def __iadd__(self, other):
        if self.rows != other.rows and self.cols != other.cols:
            raise ValueError("Matrixes has to be of same size for addition")
        for i in range(0,self.cols):
            for j in range(0,self.rows):
                self.mat[i][j] += other.mat[i][j]
    
    def __sub__(self, other):
        self.__add__(other * -1)
    
    def __isub__(self, other):
        self.__iadd__(other * -1)
    
    def __repr__(self):
        return f'Matrix {self.rows} x {self.cols}, with {type(self.mat[0][0])} elements\n'+f'{self}'
    
    def __str__(self):
        str = ''
        for  i in range(0,self.cols):
            str = str + '[\t'
            for j in range(0, self.rows):
                str = str + f'{self.mat[i][j]}' + '\t'
            str = str + ']\n'
        return str 

class Vector(Matrix):
    def __init__(self,dim):
        super.__init__(rows = dim, columns = 1)


x = Matrix(matrix=[[3,4,5],[4,5,6],[5,6,7]])
y = Matrix(matrix=[[1,2,3],[2,3,4],[4,5,6]])
code.interact(local=locals())