from audioop import mul


"""
Strings

This file talks about strings.
"""


my_string = "hello world"
print(my_string)

string_with_quotes = "Hello it's me"
another_with_quotes = 'He said "You are amaizing" yesterday.'
another_with_quotes2 = "He said \"You are amaizing\" yesterday."
multiline = """Hello, world.

I'm learning puython
"""
print(string_with_quotes)
print(another_with_quotes)
print(another_with_quotes2)
print(multiline)

name = "Jose"
greeting = "Hello, " + name
print(greeting)

age = 24
age_as_str = str(age)
print("You are " + age_as_str)
