#Class Methods = Allow operationns related to the class itself

class student:
    count = 0
    gpa_total = 0.0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        student.count += 1
        student.gpa_total += gpa
    
    #Instance Method
    def info(self):
        return f"{self.name}: {self.gpa}"
    
    @classmethod
    def get_count(cls):
        return f"Number of students: {cls.count}"
    
    @classmethod
    def get_average(cls):
        if cls.count == 0.0:
            return 0
        else:
            return cls.gpa_total / cls.count    
    
student1 = student("Jax", 2.4)
student2 = student("Ragatha", 3.3)
student3 = student("Pomni", 3.8)

print(student.get_count())
print(f"Average of this class: {student.get_average():.2f}")

#Instance Methods = Best for operations on instances of the class
#Static Methods = Best for utility functions thaat do not require access to class data
#Class Methods = Best for class-level data or require access to the class itself