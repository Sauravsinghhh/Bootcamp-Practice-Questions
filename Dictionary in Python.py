my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

print(my_dict.keys())   
print(my_dict.values())
print(my_dict.items())  

# Using pop()
value = my_dict.pop('c')
print(value)           
print(my_dict)          

# Using clear()
my_dict.clear()
print(my_dict)         

# Using copy()
original_dict = {'a': 1, 'b': 2}
copied_dict = original_dict.copy()
print(copied_dict)      


squared_dict = {key: value ** 2 for key, value in copied_dict.items()}
print(squared_dict)     

# Nested dictionaries
nested_dict = {
    'person1': {'name': 'Saurav', 'age': 20},
    'person2': {'name': 'Uttam', 'age': 19}
}

print(nested_dict['person1']['name'])
print(nested_dict['person2']['age'])   