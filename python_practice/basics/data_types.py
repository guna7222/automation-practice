
class DataTypes:

    def __init__(self, age=None, height=None):
        self.age = age
        self.height = height
        self.int_number = None

    # requirement for army selection based on age and height
    def is_eligible_for_army(self):
        if self.age is not None and self.height is not None:
            if self.age > 18 and self.height >= 170:
                return "Eligible for army selection."
            else:
                return "Not eligible for army selection."
        else:
            return "Age is not provided."

    # type conversion
    def convert_float_to_int(self, float_number):
        self.int_number = int(float_number)
        return self.int_number


data_types = DataTypes()
print(data_types.is_eligible_for_army())

print(data_types.convert_float_to_int(34.56))
