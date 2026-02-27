''' Write a program that takes the length and breadth of a rectangle as input and prints its area
and perimeter.
Note: If the inputs are invalid, display an appropriate message. '''
''' PROCESS - 1 '''
length = int(input("enter the length of rectangle (non - negative) :"))
breadth = int(input("enter the breadth of rectangle (non - negative) :"))
if length < 0 or breadth < 0:
    print("please check length or breadth is in negative integer")
else :
    area = length * breadth
    perimeter = 2 * (length + breadth)
    print(f"area of rectangle with dimensions [{length}][{breadth}] = {area}")
    print(f"perimeter of rectangle with dimensions [{length}][{breadth}] = {perimeter}")


''' PROCESS - 2 '''
def areaofrectangle(length,breadth):
    area = length * breadth
    return area
def perimeterofrectangle(length,breadth):
    perimeter = 2 * (length + breadth)
    return perimeter
length = int(input("enter the length of rectangle (non - negative) :"))
breadth = int(input("enter the breadth of rectangle (non - negative) :"))
if length < 0 or breadth < 0:
    print("please check length or breadth is in negative integer")
else:
    print(f"area of rectangle with dimensions [{length}][{breadth}] = {areaofrectangle(length,breadth)}")
    print(f"perimeter of rectangle with dimensions [{length}][{breadth}] = {perimeterofrectangle(length,breadth)}")


''' process - 3 '''
class rectangle:
    def __init__(self,length,breadth):
        self.__length = length
        self.__breadth = breadth
    def __str__(self):
        return f"entered length = {self.__length}, breadth = {self.__breadth}"
    def area_of_rectangle(self):
        if length < 0 or breadth < 0:
            return "length and breadth must not be zero."
        else:
            return f"area of the rectangle = {self.__length * self.__breadth}"
    def perimeter_of_rectangle(self):
        if length < 0 or breadth < 0:
            return "length and breadth must not be zero."
        else:
            return f"perimeter of the ractangle = {2 * (self.__length + self.__breadth)}"
length = float(input("enter length of the rectangle :"))
breadth = float(input("enter breadth of the rectangle :"))
r1 = rectangle(length, breadth)
print(r1)
print(r1.area_of_rectangle())
print(r1.perimeter_of_rectangle())