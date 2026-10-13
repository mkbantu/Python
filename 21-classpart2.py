"""diffrence btn the static method and class method
1. Static method does not take any default parameters, while class method takes cls as default parameter
2. Static method can be called using the class name or object of the class, 
    while class method can only be called using the class name
3. Static method is used to create utility functions"""

class student:
    school="university of Rwanda"
    def __init__(self, name, marks):
        self.name=name
        self.marks=marks
    #instance method
    def get_result(self):
        return f"Student Name: {self.name}, Marks: {self.marks}, School: {self.school}"
    
    #class method
    @classmethod
    def get_school(cls):  
        cls.school="university of Kenya"
        return f"School: {cls.school}"
    #static method
    @staticmethod
    def is_pass(marks):
        return "Pass" if marks>=50 else "Fail"

stud1= student("John", 80)
print(stud1.get_result())
print(stud1.get_school())
print(stud1.is_pass(80))