class phoneBook:
    """
    Documentation strnigs that describes the class
    """

    def __init__(self, name, age, numbers):
        """
        Docstring describling the function
        """
        self.name = name
        self.age = age
        self.numbers = numbers

    def printPhoneBook(self):
        return f"{self.name}'s age is {self.age} and he is at {self.location} with numbers {self.numbers}"
