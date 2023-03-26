from copy import deepcopy

class Matrix:
    def __init__(self, matrix):
        self.matrix = deepcopy(matrix)

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, list)) for list in self.matrix])

    def size(self):
        size_pair = (len(self.matrix), len(self.matrix[0]))
        return size_pair

    def __getitem__(self, idx):
        return self.matrix[idx]

    def __add__(self, other):
        other = Matrix(other)
        result = []
        num = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                summ = other[i][j] + self.matrix[i][j]
                num.append(summ)
                if len(num) == len(self.matrix):
                    result.append(num)
                    num = []
        return Matrix(result)

    def __sub__(self, other):
        other = Matrix(other)
        result = []
        num = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                sub = other[i][j] - self.matrix[i][j]
                num.append(sub)
                if len(num) == len(self.matrix):
                    result.append(num)
                    num = []
        return Matrix(result)

    def __mult_num__(self, n):
        result = []
        num = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                mult_num = self.matrix[i][j] * n
                num.append(mult_num)
                if len(num) == len(self.matrix):
                    result.append(num)
                    num = []
        return Matrix(result)

    def __mult_matrix__(self, other):
        other = Matrix(other)
        result = []
        num = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                for k in range(len(self.matrix)):
                    mult_matrix = sum(other[i][k] * self.matrix[k][j])
                    num.append(mult_matrix)
                    if len(num) == len(self.matrix):
                        result.append(num)
                        num = []
        return Matrix(result)

    def __transpose__(self):
        result = []
        num = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                transpose = self.matrix[j][i]
                num.append(transpose)
                if len(num) == len(self.matrix):
                    result.append(num)
                    num = []
        return Matrix(result)



m = Matrix([[1, 4, 5],
            [5, 8, 9],
            [6, 7, 11]])
n = Matrix([[3, 7, 4],
            [5, 4, 22],
            [5, 7, 21]])

# print(Matrix.__add__(m, n))
# print(Matrix.__sub__(m, n))
# print(Matrix.__mult_num__(m, 6))
# print(Matrix.__transpose__(m))
# print(Matrix.__mult_matrix__(m, n))



