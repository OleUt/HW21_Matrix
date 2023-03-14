class MyMatrix(object):

    def __init__(self):
        pass

    def matrix_print(self, ml):
        for i in ml:
            print(i)

    def mult_const(self, ml, c):
        a = []
        for i in ml:
            b = []
            for j in i:
                b.append(j * c)
            a.append(b)
        return a

    def plus_const(self, ml, c):
        a = []
        for i in ml:
            b = []
            for j in i:
                b.append(j + c)
            a.append(b)
        return a

    def minus_const(self, ml, c):
        c = c * (-1)
        a = self.plus_const(ml, c)
        return a

    def __count_rows_columns(self, ml):
        rows = len(ml)
        columns = 0
        for i in ml:
            columns = len(i)
        return rows, columns                # number of rows and columns

    def __total_values(self, ml):
        total = []
        for i in ml:
            for j in i:
                total.append(j)             # list containing all values
        return total

    def transpose_matrix(self, ml):
        size = list(self.__count_rows_columns(ml))
        rows, columns = size[1], size[0]                        # number of rows and columns in transposed matrix
        total = self.__total_values(ml)
        transposed = []
        for j in range(rows):
            a = []
            for i in range(j, len(total), rows):
                a.append(total[i])
            transposed.append(a)
        return transposed

    def mult_matrix_matrix(self, ml1, ml2):
        size1 = list(self.__count_rows_columns(ml1))
        rows1, columns1 = size1[0], size1[1]                    # number of rows and columns in matrix 1
        size2 = list(self.__count_rows_columns(ml2))
        rows2, columns2 = size2[0], size2[1]                    # number of rows and columns in matrix 2
        try:
            if (rows1 != columns2) or (rows2 != columns1):
                raise Exception
            else:
                tr_ml2 = self.transpose_matrix(ml2)
                d = []
                for i in range(rows1):
                    a, c = ml1[i], []
                    for j in range(rows1):
                        b, s = tr_ml2[j], 0
                        for k in range(columns1):
                            s += a[k] * b[k]
                        c.append(s)
                    d.append(c)
            return d
        except Exception:
            print("Impossible to multiply this matrices: rows and columns don't match")

    def matrix_plus_matrix(self, ml1, ml2):
        size1 = list(self.__count_rows_columns(ml1))
        rows1, columns1 = size1[0], size1[1]                    # number of rows and columns in matrix 1
        size2 = list(self.__count_rows_columns(ml2))
        rows2, columns2 = size2[0], size2[1]                    # number of rows and columns in matrix 2
        try:
            if (rows1 != rows2) or (columns1 != columns2):
                raise Exception
            else:
                d = []
                for i in range(rows1):
                    a, b, c, s = ml1[i], ml2[i], [], 0
                    for k in range(columns1):
                        s = a[k] + b[k]
                        c.append(s)
                    d.append(c)
            return d
        except Exception:
            print("Numbers of rows and columns don't match")

    def matrix_minus_matrix(self, ml1, ml2):
        negative_ml2 = self.mult_const(ml2, -1)
        d = (self.matrix_plus_matrix(ml1, negative_ml2))
        return d


my_object = MyMatrix()
my_list = [[1, 2, 3], [4, 5, 6]]

# print matrix
print('original matrix')
my_object.matrix_print(my_list)

# matrix + const
matrix_plus_const = my_object.plus_const(my_list, 10)
print('matrix + constanta')
my_object.matrix_print(matrix_plus_const)

# matrix - const
matrix_minus_const = my_object.minus_const(my_list, 5)
print('matrix - constanta')
my_object.matrix_print(matrix_minus_const)

# matrix * const
mult_matrix_const = my_object.mult_const(my_list, 2)
print('matrix * constanta')
my_object.matrix_print(mult_matrix_const)

# transposed matrix
transposed_matrix = my_object.transpose_matrix(my_list)
print('transposed matrix')
my_object.matrix_print(transposed_matrix)


my_list1 = [[1, 2], [3, 4]]
my_list2 = [[10, 20], [30, 40]]

# matrix + matrix
print('matrix + matrix')
my_object.matrix_print(my_object.matrix_plus_matrix(my_list1, my_list2))

# matrix - matrix
print('matrix - matrix')
my_object.matrix_print(my_object.matrix_minus_matrix(my_list1, my_list2))


my_list3 = [[4, 2, 1], [9, 0, 6]]
my_list4 = [[3, 1], [-3, 4], [-7, 6]]

# matrix * matrix
print('matrix * matrix')
my_object.matrix_print(my_object.mult_matrix_matrix(my_list3, my_list4))
