my_list = [2, 4, 6, 8, 9, 10]

my_list.append(10)
print(f"append 10: {my_list}")

my_list.remove(6)
print(f"remove 6: {my_list}")

my_list.reverse()
print(f"reversed: {my_list}")

my_list.sort()
print(f"sorted: {my_list}")

#

my_dict = {'a': 1, 'b': 2, 'c': 3}

my_dict['d'] = 4

my_dict['a'] = 5

removed_value = my_dict.pop('b')

value_c = my_dict.get('c')

keys = my_dict.keys()

values = my_dict.values()

items = my_dict.items()

my_dict, removed_value, value_c, list(keys), list(values), list(items)

#

my_tuple = (1, 2, 3, 4, 5)

first_element = my_tuple[0]

sub_tuple = my_tuple[1:4]

index_of_3 = my_tuple.index(3)

count_of_2 = my_tuple.count(2)

my_tuple, first_element, sub_tuple, index_of_3, count_of_2




