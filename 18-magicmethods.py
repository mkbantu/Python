class student :
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Student Name: {self.name}, Age: {self.age}"

        """Most data types (string, number, list, etc) compare by content when you use == to compare them.

    For objects, this is not the case. The == operator checks if the two variables point to the exact same object in memory - not if their content matches.

    The __eq__() method allows you to change this behavior."""


    def __eq__(self, other):
      
            return self.name == other.name and self.age == other.age


    """ Magic methods can control what happens when you use an operator, like +, on your own objects. This is called operator overloading."""
        
    def __add__(self, other):
        return self.age + other.age

    """The __len__() method controls what the built-in len() function returns for your object."""
    def __len__(self):
        return len(self.name)

    
student1 = student("John", 20)
student2 = student("John", 20)
print(student1)  # Output: Student Name: John, Age: 20
print(student2)  # Output: Student Name: John, Age: 20
print(student1 == student2)  # Output: True
print(student1 + student2)  # Output: 40
print(len(student))  # Output: 4
