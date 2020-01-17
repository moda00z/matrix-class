import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
    # def __len__(self):
       # return self.number
    
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here
        if self.h == 1 and self.w ==1:
            determ = self[0]
            return value
        if self.h == 2 and self.w == 2:
            determ = self[0][0] * self[1][1] - self[1][0] * self[0][1]
            return determ
    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here
        total = 0
        for i in range(self.h):
            for j in range(self.w):
                if i == j:
                    total += self[i][j]
        return total
    
    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        # TODO - your code here
        invM = zeroes(self.h, self.w)
        if self.h == 1 and self.w == 1:
            invM[0][0] = 1/self[0][0]
            return invM
        if self.h == 2 and self.w == 2:
            determ = self.determinant()
            invM = [[self[1][1]/determ, -1*self[0][1]/determ], [-1*self[1][0]/determ, self[0][0]/determ]]
            return Matrix(invM)
    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        rows = self.h
        cols = self.w
        Tmat = zeroes(cols, rows) # Tmat is zeros matrix with the transposed dimentions
        for i in range(rows):
            for j in range(cols):
                Tmat[j][i] = self[i][j]
        return Tmat
    
    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        #
        sumM = zeroes(self.h, other.w)
        for i in range(self.h):
            for j in range(other.w):
                sumM[i][j] = self[i][j] + other[i][j]
                
        return sumM
                
    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        #
        negM = zeroes(self.h, self.w)
        for i in range(self.h):
            for j in range(self.w):
                negM[i][j] = -1 * self[i][j]
        return negM
        
    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here
        #
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be subtracted if the dimensions are the same")
            
        subM = zeroes(self.h, other.w)
        for i in range(self.h):
            for j in range(other.w):
                subM[i][j] = self[i][j] - other[i][j]
        return subM
    
    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        #
       # if self.w != other.w:
          #  raise(ValueError, " Number of columns must be equal to multiply")
        mulM = zeroes(self.h, other.w)
        for i in range(self.h):
            for j in range(other.w):
                total = 0
                for ii in range(self.w):
                    total += self[i][ii] * other[ii][j]
                mulM[i][j] = total
        return mulM   
        

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            pass
            #   
            # TODO - your code here
            #
            rmulM = zeroes(self.h, self.w)
            for i in range(self.h):
                for j in range(self.w):
                    rmulM[i][j] = other * self[i][j]
                    
            return rmulM       
            