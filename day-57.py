class Person:
    def __init__(self, name, job, salary):
        self.name = name
        self.job = job
        self.__salary = salary

    def printSalary(self):
        print(f"Salary of {self.name} is {self.__salary}")


harry = Person("Harry", "Software Engineer", 200000)
print(harry.name)
print(harry.job)
# print(harry.salary) # private variables can't be accessed from outside of the class
harry.printSalary()

print()

shubham = Person("Shubham", "Fullstack Web Developer", 150000)
print(shubham.name)
print(shubham.job)
# print(shubham.salary) # private variables can't be accessed from outside of the class
shubham.printSalary()