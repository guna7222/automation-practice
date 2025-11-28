"""
Naming convention of variables:
- a variable must start with a letter (a - z, A - Z) or an underscore (_)
- a variable cannot start with a number (0 - 9)
- a variable can only contain alphanum                     eric characters and underscores (A - Z, a - z, 0 - 9, and _ )
- variable names are case-sensitive (age, Age and AGE are three different variables)
"""

# variables are containers for storing data values
# in python the variables are created the moment you a value for it
class Variables:

    # class variables
    eligible_age = 18

    def __init__(self):
        self.name = None  # instance variable
        self.age = None
        self.amount = None
        self.price = None
        self.price_float = None

    def is_eligible_for_driving_license(self, name, age):
        self.name = name
        self.age = age

        if self.age >= Variables.eligible_age:
            return f"{self.name} is eligible for a driving license."
        else:
            return f"{self.name} is not eligible for a driving license."

    def casting_example(self, amount):
        self.amount = amount
        # casting
        self.price = int(self.amount)
        # converting int to float
        self.price_float = float(self.price)
        print(type(self.amount))
        print(type(self.price_float))
       


variables = Variables()
print(variables.is_eligible_for_driving_license("Guna", 19))
variables.casting_example("1500")

