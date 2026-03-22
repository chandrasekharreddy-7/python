# list
class my_list():
    def __init__(self):
        self.l = [0,0,0,0,0,0,0,0,0,0]
        self.count = 0
    def my_append(self, value):
        self.l[self.count] = value
        self.count += 1
    def print_list(self):
        print("[",end = "")
        for i in range(self.count):
            if i != self.count - 1:
                print(self.l[i], end = ",")
            else:
                print(f"{self.l[i]}]",end = " ")
    def insert(self, value, index):
        i = self.count
        while i > index:
            self.l[i] = self.l[i - 1]
            i -= 1
        self.count += 1
        self.l[index] = value
    def deletebypos(self):
        n = self.count
        pos = int(input("Enter position to delete: "))
        if pos < 1 or pos > n:
            print("Invalid position!")
            return
        for i in range(pos - 1, n - 1):
            self.l[i] = self.l[i + 1]
        self.count = n - 1
        print(f"List after deleting element at position {pos}")
        print("[", end="")
        for i in range(self.count):
            if i != self.count - 1:
                print(self.l[i], end=",")
            else:
                print(f"{self.l[i]}]\n", end="")
    def deleteusingnewlist(self):
        pos = int(input("enter position to delete element :"))
        if pos < 1 or pos > self.count:
            print("Invalid position")
            return
        self.newl = []
        for i in range(self.count):
            if i != pos - 1:
                self.newl.append(self.l[i])
        print("List after deletion:", self.newl)
    def deletebyvalue(self):
        value = input("Enter value to delete: ")
        pos = -1
        for i in range(self.count):
            if str(self.l[i]) == value:
                pos = i
                break
        if pos == -1:
            print("Value not found!")
            return
        for i in range(pos, self.count - 1):
            self.l[i] = self.l[i + 1]
        self.count -= 1
        print("List after deleting value:", end=" ")
        self.print_list()
        print()
    def deletealloccurrences(self):
        value = input("Enter value to delete: ")
        i = 0
        while i < self.count:
            if str(self.l[i]) == value:
                for j in range(i, self.count - 1):
                    self.l[j] = self.l[j + 1]
                self.count -= 1
            else:
                i += 1
        print("list after deleting all occurrences:", end=" ")
        self.print_list()
        print()
l1 = my_list()
l1.my_append(4)
l1.my_append(64)
l1.my_append(24)
l1.my_append(24)
l1.my_append("CHANDRA")
l1.my_append("SIVA")
print("Original list:", end=" ")
l1.print_list()
print()
l1.deletealloccurrences()