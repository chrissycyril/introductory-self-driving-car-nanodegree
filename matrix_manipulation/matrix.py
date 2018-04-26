import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for __ in range(width)] for __ in range(height)]
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
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here
        
        if(self.h==1):
            #print(self.g[0])
            #print(self.g[0][0])
            return (self.g[0][0])
            
        else:
            if(self.g[0][0]*self.g[1][1]==self.g[0][1]*self.g[1][0]):
                raise ValueError('The denominator of a fraction cannot be zero')
            else:
                det=self.g[0][0]*self.g[1][1]-self.g[0][1]*self.g[1][0]
                #print(det)
                return det
                    
                
    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")
       
        # TODO - your code here
        
        sum=0
        for i in range(self.h):
            sum=sum+self.g[i][i]
        return sum
            
    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")
       
        # TODO - your code here
        inv=[]
        inverse=[]
        
        if(self.h==1):
            #print(self.determinant())
            inverse.append([1/self.determinant()])
            return Matrix(inverse)
        
        else:
            p=self.determinant()
            inv.append(self.g[1][1]*1/p)
            inv.append(-1*(self.g[0][1])*1/p)
            inverse.append(inv)
            inv=[]
            inv.append(-1*(self.g[1][0])*1/p)
            inv.append(self.g[0][0]*1/p)
            inverse.append(inv)
            return Matrix(inverse) 
    
    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        matrix_transpose = []
     
        for i in range (self.w):
            matrix_trans = []
            for j in range (self.h):
                matrix_trans.append(self.g[j][i])
            matrix_transpose.append(matrix_trans)
    
        return Matrix(matrix_transpose)

    def is_square(self):
    
        return (self.h == self.w)

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
        matrixSum=[]
        
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        
        else:
                       
            for i in range (self.h):
                row=[]
                for j in range (self.w):
            
                    row.append(self.g[i][j]+other.g[i][j])
                matrixSum.append(row)
        return (Matrix(matrixSum))
               
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
        negative=[]
        row=[]
        for i in range (self.h):
            row=[]
            for j in range (self.w):
                row.append(-(self.g[i][j]))
            negative.append(row)
        return Matrix(negative)
    
    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        
        #   
        # TODO - your code here
        #
        matrixDiff=[]
        
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be subtracted if the dimensions are the same") 
           
        
        else:
                       
            for i in range (self.h):
                row=[]
                for j in range (self.w):
            
                    row.append(self.g[i][j]-other.g[i][j])
                matrixDiff.append(row)
        return Matrix(matrixDiff)
    
    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        a=zeroes(self.h,other.w)
        for i in range (self.h):
                value= 0
                row_result= []
                for j in range(other.w):
                    value= 0
                    for y in range(self.w):
                        a[i][j]=a[i][j]+self.g[i][y]*other.g[y][j]
        return a
               
        

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
            
            for i in range (self.h):
                for j in range(self.w):
                    self.g[i][j] *= other
                
            return self