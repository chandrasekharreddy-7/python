''' Vector Class Implementation: Create a class Vector representing an n-dimensional vector that supports:
Printing the vector.
Scalar multiplication ($2 * v$).
Vector addition and subtraction ($v1 + v2$ and $v1 - v2$). '''
class Vector:
    def __init__(self, values):
        self.values = values
    def __str__(self):
        return str(self.values)
    def __add__(self, other):
        result = []
        for i in range(len(self.values)):
            result.append(self.values[i] + other.values[i])
        return Vector(result)
    def __sub__(self, other):
        result = []
        for i in range(len(self.values)):
            result.append(self.values[i] - other.values[i])
        return Vector(result)
    def __rmul__(self, scalar):
        result = []
        for i in self.values:
            result.append(scalar * i)
        return Vector(result)
v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])
print("v1:", v1)
print("v2:", v2)
print("addition:", v1 + v2)
print("subtraction:", v1 - v2)
print("scalar multiplication:", 2 * v1)