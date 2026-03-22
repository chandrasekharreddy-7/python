class Vector:
    def __init__(self, values):
        self.values = values   # list of numbers
    def __str__(self):
        return str(self.values)
    def scalar_mul(self, scalar):
        result = []
        for x in self.values:
            result.append(x * scalar)
        return Vector(result)
    def add(self, other):
        if len(self.values) != len(other.values):
            return f"please enter correct choice."
        result = []
        for i in range(len(self.values)):
            result.append(self.values[i] + other.values[i])
        return Vector(result)
    def subtract(self, other):
        if len(self.values) != len(other.values):
            return f"please enter correct choice."
        result = []
        for i in range(len(self.values)):
            result.append(self.values[i] - other.values[i])
        return Vector(result)
    def dot(self, other):
        if len(self.values) != len(other.values):
            return f"please enter correct choice."
        result = 0
        for i in range(len(self.values)):
            result += self.values[i] * other.values[i]
        return result
v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])
print("v1:", v1)
print("v2:", v2)
print("scalar multiplication:", v1.scalar_mul(2))
print("addition:", v1.add(v2))
print("subtraction:", v1.subtract(v2))
print("dot product:", v1.dot(v2))