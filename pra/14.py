''' Student and Score Classes: 
    Create classes Score and Student where the Student class supports storing a name,
    list of courses, and scores, while also providing methods to print details and compute averages. '''
class Score:
    def __init__(self, course, marks):
        self.course = course
        self.marks = marks
class Student:
    def __init__(self, name):
        self.name = name
        self.scores = []
    def add_score(self, course, marks):
        s = Score(course, marks)
        self.scores.append(s)
    def print_details(self):
        print("student Name:", self.name)
        print("courses and Marks:")
        for s in self.scores:
            print(s.course, ":", s.marks)
    def average(self):
        total = 0
        for s in self.scores:
            total += s.marks
        if len(self.scores) == 0:
            return 0
        return total / len(self.scores)
s1 = Student("chandra")
s1.add_score("math", 90)
s1.add_score("science", 80)
s1.add_score("english", 85)
s1.print_details()
print("average:", s1.average())