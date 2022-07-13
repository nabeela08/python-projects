from inspect import Parameter


def greet_with_name(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

greet_with_name("Nabeela", "Sweden")
# greet_with_name("Sweden", "Nabeela") #positional parameter

# to solve this positional parameter problem we can use keyword argumanets
greet_with_name(location= "Sweden", name= "Nabeela")
