

class DictionaryExample:

    def __init__(self, data=None):
        if data is not None:
            self.data = data
        else:
            self.data = {}


    def print_dictionary(self):
        print(self.data)

    def changing_values(self):
        self.data["name"] = "Kumar"
        self.data.update({"age": 30})
        print(self.data)

    def looping_through_dict(self):
        if "name" in self.data:
            print("Yes, 'name ' is one of the keys in the dictionary")
        for key, value in self.data.items():
            print(f"{key} : {value}")

        # removing random key-value pair
        print(self.data.popitem())

# items()
# values()
# keys()
# pop('key')
# popitem()
# update({'key': 'value'})
# get('key')
# clear()
# del dict['key']
# del dict
# copy()


dict_example = DictionaryExample({"name": "Guna", "age": 25, "city": "Chennai"})
dict_example.print_dictionary()
dict_example.changing_values()
dict_example.looping_through_dict()