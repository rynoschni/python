import random

eightball_choices = {
    "1": "outlook unclear",
    "2": "looks good to me",
    "3": "Foo",
    "4": "Bar",
    "5": "Baz"
}

random_selection = eightball_choices[str(random.randint(1,5))]

print(random_selection)