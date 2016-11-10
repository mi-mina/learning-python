import random
import sys
import os
import numpy as np

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

print('\n'*2)

# Functions and methods *****************************************************
# There are built-in functions, like max()
# And there are methods, that are specific to each type of object. The call functions
# on objects.

# Some methods don't change the object they're called on, but others do.
# (Como en Javascript)
# help(str) to get the docs of a method

print('Functions and methods *********************************')
string1 = 'room'
print(string1.upper())
print('There are ', string1.count('o'), 'Os in', string1)

areas = [10, 20, 15, 25, 30, 35, 15, 20]

# The index method returns the index of the first element found that matches the arguments
print(areas.index(20))
# Counts the frequency of an element in a list
print(areas.count(20))

areas.append(21)
print(areas)

areas.remove(20)
print(areas)

areas.reverse()
print(areas)

print('\n'*2)

# Numpy Arrays ***************************************
# Numpy arrays allows you to make operations over an entire array

# This is a list
measures = [180, 215, 210, 210, 188, 176, 209, 200]

# This is an array
np_measures = np.array(measures)
print(type(np_measures))

# If I multiply a list by a number N it returns a new list with N times its elements
print(measures*2)

# If I multiply an array by a number, it does the operation element-wise.
# It's like if we were using map + operator in clojure
# It's the behaviour by default in a R vector
print('An array multiplied by a number', np_measures*2)

measures2 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
measures3 = np.array([1, 2, 3, 4, 5, 6, 7])

# We can divide 2 arrays element-wise if they have the same shape
print('Division element-wise of 2 arrays of the same shape', np_measures / measures2)
# print(np_measures / measures3) This will throw an error

print('Multiplication element-wise of 2 arrays of the same shape', np_measures * measures2)

# This returns a boolean vector
print(np_measures < 200)
# This returns a sliced vector with the elements that match the condition
print(np_measures[np_measures < 200])

# Numpy arrays can not contain elements with different types. If we try this:
mixed_array = np.array([1, False, 3])
mixed_array2 = np.array(['one', False, 3])
# mixed_array will be created with no error, but some of the
# elements' types are changed to end up with a homogeneous list
# It's called Type coercion
print(mixed_array)  # Array of numbers
print(mixed_array2)  # Array of strings

np_mat = np.array([[1, 2],
                   [3, 4],
                   [5, 6]])
np_mat * 2

# Note how + behaves differently
np_mat + np.array([10, 10])
np_mat + np_mat

# Generate data
# np.random.normal(mean, distribution standard deviation, number of samples)
heights = np.round(np.random.normal(1.75, 0.2, 5000), 2)
weights = np.round(np.random.normal(60.5, 20, 5000), 2)
# np.column_stack(tupple)
np_population = np.column_stack((heights, weights))

mean_heights = np.mean(np_population[:,0])
print('mean_heights', mean_heights)

median_heights = np.median(np_population[:, 0])
print('median_heights', median_heights)

# Standard deviation
std_weights = np.std(np_population[:, 1])
print('std_weights', std_weights)

# Correlation coef
corr = np.corrcoef(np_population[:, 0], np_population[:, 1])
print('corr', corr)


fat_heights = heights[weights > 120]
print(len(fat_heights))
print(max(weights))