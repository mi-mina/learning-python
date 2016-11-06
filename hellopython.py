import random
import sys
import os

print("hello world")

# This is a comment

'''
Multiline
comment
'''

name = 'Espe'
print(name)

# semicolons in python are used to place commands on the same line
last_name = 'Smith'; print(last_name)

# Strings, numbers, lists, tuples and dictionaries

# operations
# + - * /
# % modulus. returns the remainder of a division
# ** exponential calculation
# // performs the division and discards the remainder. Ej 7//2 = 3

print('5 % 2 = ', 5 % 2)
print('5 ** 2 = ', 5 ** 2)
print('7 // 2 = ', 7 // 2)

# Order of operations matters

quote = "\" Forget everything, "  # Use \ to escape

multi_line_quote = ''' not
just something." '''

# variables with more than one word are usually written with underscores

print(quote+multi_line_quote)

# Format
print('%s %s %s' % ('Somebody told me,', quote, multi_line_quote))

print('This is the first part of a sentence, ', end='')  # no tentiendo este end para qué sirve
print('this is the second part.')

# sep adds an element as a separator
print('hola', 'adios', '¿qué tal?', sep=', ', end='Creo que añade algo al final')

print('\n'*2)

# Lists ***************************************************************
print('Lists ***************************************************')

groceries_list = ['bananas', 'avocados', 'oranges',
                  'butter', 'nuts', 'tomatos', 'eggs']
print('first item: ', groceries_list[0])

groceries_list[0] = 'juice'  # to change a value in a list (mutable)
print('first item updated: ', groceries_list[0])
# You can change several elements at once
groceries_list[:2] = ['lemons', 'apples']
print('groceries_list changed ', groceries_list)

# We can also use negative indexes. -1 returns the last element
print('the last element of the list is ', groceries_list[-1])
print('the before last element of the list is ', groceries_list[-2])

# subset of a list: slicing
print('subset of a list: ', groceries_list[1:3])  # from 1 up to 3 not included
print('from element 0 up to the third not included', groceries_list[:3])
print('from the second element up to the end of the list ', groceries_list[2:])
print('the last 3 elements of the list ', groceries_list[-3:])


other_events = ['read books', 'watch movies']
to_do_list = [groceries_list, other_events]  # List of lists
print('list of lists', to_do_list)
print('first element of the second list: ', to_do_list[1][0])
print('sum of lists', groceries_list + other_events)


groceries_list.append('onions')
groceries_list.insert(1, 'potatos')
groceries_list.remove('oranges')
print(groceries_list)

groceries_list.sort()
print(groceries_list)

groceries_list.reverse()
print(groceries_list)

del groceries_list[0]  # It can be also written like this: del(groceries_list[0])
print('groceries_list after deleting the first element ', groceries_list)

to_do_list2 = groceries_list + other_events
print(to_do_list2)
print(len(to_do_list2))
print(max(to_do_list2))  # the one that comes first alphabetically
print(min(to_do_list2))  # the one that comes last alphabetically

# You can mix types in a list
mixed_list = [1.2, 2, 'two', True]
print('mixed_list ', mixed_list)

# More on lists manipulation and mutability
x = [1, 2, 3]
print('x ', x)
# We create a new variable to store a 'copy' of the first list
# But what we are really copying is a reference to that variable
y = x
print('y ', y)

# So, if we change y, we are also changing x
y[1] = 5
print('y changed', y)
print('x changed indirectly', x)

# If we want a copy of x and not of its reference, we can do this:
z = list(x)
print('z', z)

z[1] = 10
print('z changed', z)
print('x unchanged', x)

# Another way
s = x[:]
print('s', s)

print('\n'*2)

# Tuples ********************************************************
# Theyre very similar to lists, but we're not going to be able to change a tuple after
# it is created
print('Tuples ***************************************************')

my_tuple = (1, 2, 3, 4)

# If you want to convert a tuple into a list
new_list = list(my_tuple)

print(len(my_tuple))
print(min(my_tuple))
print(max(my_tuple))
print('primer elemento de my_tuple ', my_tuple[0])

print('\n'*2)

# Dictionaries *************************************************
print('Dictionaries ***************************************************')

alimentos = {'naranja': 'fruta',
             'zanahoria': 'hortaliza',
             'arroz': 'cereal',
             'garbanzo': 'legumbre',
             'trigo sarraceno': 'cereal'}

print('la naranja es una ', alimentos['naranja'])

del alimentos['zanahoria']
print(alimentos)

# To change the value of an item attached to a key
alimentos['trigo sarraceno'] = 'legumbre'
print(alimentos)

# We can have lists of lists inside a dictionary
mixed_data_structure = {'family': [['liz', 1.6], ['tom', 1.8]],
                        'friends': [['mary', 1.6], ['john', 1.8]]}
print('mixed_data_structure', mixed_data_structure)


# Functions and methods *****************************************************
# There are built-in functions, like max()
# And there are methods, that are specific to each type of object. The call functions
# on objects.

