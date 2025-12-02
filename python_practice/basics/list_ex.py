from turtledemo.penrose import start


class ListExample:

    def __init__(self, items=None):
        if items is not None:
            self.items = items
            self.numbers = [10, 20, 10, 60, 20, 60, 30, 40, 50]
        else:
            self.items = []

    def length_of_list(self):
        return len(self.items)

    # def replace_last_item(self, new_item):
    #     self.items[-1] = new_item
    #     print(self.items)

    # reverse the list
    def reverse_list(self):
        new_list = []
        new_list = self.items[::-1]
        print(new_list)

    # count banana how many times in the list
    def count_banana(self):
        count = 0
        for x in self.items:
            if x == 'banana':
                count += 1
        return count

    # length of a list without using len() function
    def length_of_list_without_len(self):
        length = 0
        for x in self.items:
            length += 1
        return length

    # max element
    def max_element(self):
        max_value = self.numbers[0]
        for num1 in range(1, len(self.numbers)):
            if self.numbers[num1] > max_value:
                max_value = self.numbers[num1]
        return max_value

    # min element
    def min_element(self):
        min_value = self.numbers[0]
        for num2 in range(1, len(self.numbers)):
            if self.numbers[num2] < min_value:
                min_value = self.numbers[num2]

        return min_value

    # print all elements in a list using for loop
    def print_all_elements(self):
        for item in self.numbers:
            print(item)

    # copy list items manually
    def copy_list_items(self):
        copy_of_items = []
        for items in self.items:
            copy_of_items.append(items)
        print(copy_of_items)

    # remove duplicates from the list
    def remove_duplicates(self):
        unique_values = []
        for i in self.numbers:
            if i not in unique_values:
                unique_values.append(i)

        return unique_values


list_example = ListExample(['apple', 'banana', 'cherry', 'banana'])
print(list_example.items)
print(list_example.length_of_list())
# list_example.replace_last_item('orange')
list_example.reverse_list()
print(list_example.count_banana())
print(list_example.length_of_list_without_len())
print(list_example.max_element())
print(list_example.min_element())
list_example.copy_list_items()
print(list_example.remove_duplicates())