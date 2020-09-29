class Matrix:
    
    
    def __init__(self, rows: int, cols: int, matrix: list) -> None:
        self.rows = rows
        self.cols = cols
        self.matrix = matrix
        
        
    def add_matrix(self: object, other_matrix: object) -> list or str:
      '''
      takes another matrix object and adds it to the matrix of self  if they have 
      an equal amount or rows and columns
      '''
      if self.rows == other_matrix.rows and self.cols == other_matrix.cols:
          return [[self.matrix[i][j] + other_matrix.matrix[i][j] 
                  for j in range(self.cols)] 
                  for i in range(self.rows)]
      else:
          return "The operation cannot be performed."
                
            
    def multiply(self: object, number: int or float) -> list:
      '''
      multiplies the matrix by a given number.
      '''
      return [[self.matrix[i][j] * number for j in range(self.cols)] for i in range(self.rows)]
        
    
    def multiply_matrix(self, other_matrix) -> list or str:
      '''
      multiplies two matrices together
      '''
      if self.cols == other_matrix.rows:
        return [[sum(self.matrix[i][k] * other_matrix.matrix[k][j] 
                      for k in range(other_matrix.rows))
                      for j in range(other_matrix.cols)] 
                      for i in range(self.rows)]
      else:
        return "The operation cannot be performed."
          
            
    def transpose_matrix(self: object, trans_choice: str) -> list:
      '''
      transposes a matrix given a user choice
      1. main diagonal
      2. side diagonal
      3. vertical line
      4. horizontal line
      '''
      if trans_choice == '1':
          return [[self.matrix[i][j] for i in range(self.cols)] for j in range(self.rows)]
      elif trans_choice == '2':
          return [[self.matrix[i][j] for i in range(self.cols - 1, -1, -1)] for j in range(self.rows - 1, -1, -1)]
      elif trans_choice == '3':
          [row.reverse() for row in self.matrix]  # reverse() changes the actual list. sucks should change so it returns a seperate list
          return self.matrix
      elif trans_choice == '4':
          self.matrix.reverse()  # reverse() changes the actual list. sucks should change so it returns a seperate list
          return self.matrix
      return 0
    
    
    def find_self_determinant(self: object) -> int or float:
      '''
      finds the determinant of the matrix object
      '''
      return Matrix.find_determinant(self.matrix)
    
    
    def find_determinant(matrix: list) -> int or float:
      '''
      finds the determinant recursively of a matrix given as a list
      '''
      if len(matrix) < 2:
          return matrix[0][0]
      elif len(matrix) == 2:
          return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
      else:
          sum_ = 0 
          target_row = 0  # target row can be specified as any row can be used to find the determinant of the matrix
          for i in range(len(matrix[target_row])):
              det_minor = Matrix.find_det_minor(matrix, target_row, i)
              sum_ += (matrix[target_row][i] * Matrix.find_cofactor(target_row, i, det_minor))
          return sum_
      return 0
    
    
    def find_minor(matrix: list, target_row: int, target_col: int) -> list:
      '''
      returns the minor of a given element, which is specified by target_row and target_col
      '''
      matrix_size = len(matrix)
      minor = [[matrix[i][j] for j in range(matrix_size) if i != target_row and j != target_col] for i in range(matrix_size)]
      return [row for row in minor if row]
        

    def find_det_minor(matrix: list, target_row: int, target_col: int) -> int or float:
      return Matrix.find_determinant(Matrix.find_minor(matrix, target_row, target_col))


    def find_cofactor(target_row: int, target_col: int, determinant: int or float) -> int or float:
      '''
      returns the cofactor of an element in the matrix using the determinant of the minor
      and the indices of the target element.  
      '''
      return((-1) ** (target_row + 1 + target_col + 1) * determinant)
        

    def find_inverse(self: object) -> list:
      '''
      returns the inverse using the equation 1/det(A) * Ct
      A = matrix
      Ct = is the transposition along the main diagonal of the cofactor matrix
      '''
      cf_list = self.cofactor_list()
      trans_cf = [[cf_list[i][j] for i in range(self.cols)]
                  for j in range(self.rows)]
      determinant = self.find_self_determinant()
      return [[trans_cf[i][j] * 1 / determinant for j in range(self.cols)] for i in range(self.rows)]
    

    def cofactor_list(self: object) -> list:
      '''
      returns the cofactor matrix of the original matrix
      '''
      mat_len = len(self.matrix)
      cf_list = [[(-1) ** (target_row + 1 + target_col + 1) * Matrix.find_det_minor(self.matrix, target_row, target_col) 
                for target_col in range(mat_len)]
                for target_row in range(mat_len)]
      return cf_list
                
                
    def make_matrix(rowcol_string: int, matrix_string: int) -> list:
        '''
        returns grabs user input and returns a Matrix object using that input
        '''
        print(f'{rowcol_string}')
        row, col = [int(n) for n in input().split()]
        print(f'{matrix_string}')
        matrix = [[int(n) if n.isdigit() else float(n) for n in input().split()] for _ in range(row)]

        return Matrix(row, col, matrix)

     
    def print_matrix(matrix) -> None:
        if isinstance(matrix, str):
            print(matrix)
        else:
            print("The result is: ")
            for row in matrix:
                print(' '.join((str(element) for element in row)))
    

    def menu():

      while True:

        print("1. Add matrices")
        print("2. Multiply matrix by a constant")
        print("3. Multiply matrices")
        print("4. Transpose matrix")
        print("5. Calculate a determinant")
        print("6. Inverse a matrix")
        print("0. Exit")
    
        choice = input("Your choice: ")
    
        if choice == '1':

            matrix_one = Matrix.make_matrix("Enter size of first matrix: ", "Enter first matrix: ")
            matrix_two = Matrix.make_matrix("Enter size of second matrix: ", "Enter second matrix: ")

            Matrix.print_matrix(matrix_one.add_matrix(matrix_two))  
            continue

        elif choice == '2':

            matrix_one = Matrix.make_matrix("Enter size of matrix: ", "Enter matrix")
            print("Enter constant: ")
            const = input()
            const = int(const) if const.isdigit() else float(const)

            Matrix.print_matrix(matrix_one.multiply(const))
            continue

        elif choice == '3':

            matrix_one = Matrix.make_matrix("Enter size of first matrix: ", "Enter first matrix: ")
            matrix_two = Matrix.make_matrix("Enter size of second matrix: ", "Enter second matrix: ")

            Matrix.print_matrix(matrix_one.multiply_matrix(matrix_two))
            continue

        elif choice == '4':

            print("1. Main diagonal")
            print("2. Side diagonal")
            print("3. Vertical line")
            print("4. Horizontal line")

            trans_choice = input(f"Your choice: ")
            matrix_one = Matrix.make_matrix("Enter size of matrix: ", "Enter matrix: ")

            Matrix.print_matrix(matrix_one.transpose_matrix(trans_choice))
            continue

        elif choice == '5':

            matrix_one = Matrix.make_matrix("Enter matrix size: ", "Enter matrix: ")
            print("The result is: ")

            print(matrix_one.find_self_determinant())
            continue

        elif choice == '6':

            matrix_one = Matrix.make_matrix("Enter matrix size: ", "Enter matrix: ")

            Matrix.print_matrix(matrix_one.find_inverse())
            continue

        else:
            break


def main():
  Matrix.menu()


# if __name__ == '__main__':
main()
