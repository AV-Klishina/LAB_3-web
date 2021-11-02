class Matrix:

    def __init__(self, *mater):
        if len(mater) == 0:
            mater = [[1, 2],
                     [3, 4]]
        self.mater = list(mater)

    def __getitem__(self, item):
        if isinstance(item, int):
            return self.mater[item]
        else:
            i, j = item
            return self.mater[i][j]

    def __setitem__(self, key, value):
        if isinstance(key, int):
            if not isinstance(value, int):
                self.mater[key] = value
        elif isinstance(value, int) and not isinstance(key, int):
            i, j = key
            self.mater[i][j] = value

    def det(self):
        mater = self.mater
        return mater[0][0] * mater[1][1] - mater[0][1] * mater[1][0]

    def __eq__(self, other):
        return self.det() == other.det()

    def __ne__(self, other):
        return self.det() != other.det()

    def __lt__(self, other):
        return self.det() < other.det()

    def __gt__(self, other):
        return self.det() > other.det()

    def __le__(self, other):
        return self.det() <= other.det()

    def __ge__(self, other):
        return self.det() >= other.det()

    def __neg__(self):
        mater = self.copy()
        for row in range(len(mater)):
            for it in range(len(mater[row])):
                mater[row, it] *= -1
        return mater

    def __str__(self):
        mater = ''
        for row in self.mater:
            mater += str(row) + '\n'
        return mater

    def __len__(self):
        return len(self.mater)

    def copy(self):
        mater = []
        for item in self.mater:
            mater.append(item.copy())

        return Matrix(*mater)

    def __add__(self, other):
        mater = self.copy()
        for row in range(len(self)):
            for it in range(len(self[row])):
                mater[row, it] += other[row][it]

        return mater

    def __sub__(self, other):
        mater = self.copy()
        for row in range(len(self)):
            for it in range(len(self[row])):
                mater[row, it] -= other[row][it]

        return mater

    def __mul__(self, other):
        mater = []
        for i in range(len(self)):
            mater.append([])
            for j in range(len(other[i])):
                mater[i].append(0)

        mater = Matrix(*mater)

        for mainRow in range(len(mater)):
            for mainIndex in range(len(mater[mainRow])):
                for index in range(len(mater[mainRow])):
                    mater.mater[mainRow][mainIndex] += (self[mainRow][index] * other[index][mainIndex])

        return mater


m = Matrix([1, 2],
           [3, 4])
m2 = Matrix([1, 2],
            [5, 3])

print(-m)
print(m * m2)
print(m2 * m)
print(m + m2)
print(m - m2)

print(f"{m.det()} > {m2.det()} is {m > m2}")
