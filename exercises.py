# Exercise 0: Example
#
# This is a practice exercise to familiarize you with basic Python data structures.
#
# Create a list called `example_list` and append three elements to it. Print each element using a loop.
#
# Requirements:
# - The list should contain any three elements of your choice.
# - Use a loop to print each element.

def example_list_function():
    example_list = ['element1', 'element2', 'element3']
    for element in example_list:
        print(element)

# Call the function and print each element
# example_list_function()


# Exercise 1: List and Indexing
#
# Create a list named students containing at least three student names (strings).
# Assign the second student’s name to a variable named first_student.
# Assign the last student’s name to a variable named last_student.

students = ['ben', 'ashley', 'jim']


def manage_students():
    first_student = students[1]
    last_student = students[-1]
    return first_student, last_student


# Call the function and print the result
print('Exercise 1:', manage_students())


# Exercise 2: Loop and String Concatenation
#
# Create a tuple named foods containing the same number of foods (strings) as there are names in the students list.
# Create a variable named meal and assign an empty string to it.
# Use a for loop to iterate over the strings in foods and append each string to meal.

foods = ('potatoes', 'eggs', 'bacon')


def combine_foods():
    meal = ''
    for food in foods:
        meal += food + ' '
    return meal


# Call the function and print the result
print('Exercise 2:', combine_foods())


# Exercise 3: Slicing Tuples
#
# Using the slice operator, assign a new tuple containing only the last two food strings in the foods to a variable named last_two_foods.

def slice_foods():
    last_two_foods = foods[slice(1, 3)]
    return last_two_foods


# Call the function and print the result
print('Exercise 3:', slice_foods())


# Exercise 4: Dictionaries and String Formatting
#
# Create a dictionary named home_town containing the keys of city, state, and population.
# Using the home_town dictionary, assign to a variable named home_town_message a string with this format: “I was born in <city>, <state> - population of <population>”

home_town = {
    'city': 'boston',
    'state': 'massachusetts',
    'pop': 'at least 12'
}

def hometown_info():
    home_town_message = 'I was born in {city}, {state} - population of {pop}'.format(**home_town)
    return home_town_message


# Call the function and print the result
print('Exercise 4:', hometown_info())
# print(home_town.values())


# Exercise 5: Iterating Over Dictionary Items
#
# Define an empty list named home_town_items.
# Use a for loop to iterate over the key: value pairs in the home_town dictionary and append a string with the following format to home_town_items: "<key> = <value>"

home_town_items = []

def list_home_town_items():
    for key, value in home_town.items():
        home_town_items.append('{} = {}'.format(key, value))
    return home_town_items


# Call the function and print the result
print('Exercise 5:', list_home_town_items())


# Exercise 6: Celebrate Students
#
# Using the list of students and a list comprehension, assign to a variable named awesome_students a new list containing strings.
# For example: ["Tina is awesome!", "Fred is awesome!", "Wilma is awesome!"]

def create_awesome_students():
    awesome_students = [f'{s} is awesome' for s in students]
    return awesome_students


# Call the function and print the result
print('Exercise 6:', create_awesome_students())


# Exercise 7: Filter Foods
#
# Assign to a variable named foods_with_an_a the result of list comprehension that filters the foods tuple to only include food strings that contain the letter 'a'.
# For example, if foods is a tuple of ('Taco', 'Burrito', 'Sandwich'), foods_with_an_a would be a list equal to ['Taco', 'Sandwich']

def filter_foods_with_a():
    foods_with_an_a = [f for f in foods if 'a' in f] # not checking for casing
    return foods_with_an_a


# Call the function and print the result
print('Exercise 7:', filter_foods_with_a())
