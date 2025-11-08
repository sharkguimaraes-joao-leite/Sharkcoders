#Static Methods = Method that belongs to a class rather than to any object in that class

class employee:
    def __init__(self, name, job):
        self.name = name 
        self.job = job

    def info(self):
        return f"{self.name}: {self.job}"
    
    @staticmethod
    def is_valid(job):
        job = job.lower()
        valid = ["Manager", "Cook", "Server", "Cashier"]
        return job.capitalize() in valid

print(employee.is_valid("Scientist"))

employee1 = employee("Steve", "Manager")
employee2 = employee("Cristhinne", "Cook")
employee3 = employee("David", "Server")

print(employee1.info())
print(employee2.info())
print(employee3.info())