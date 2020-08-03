import random

eightball_choices = {
    "option1": "outlook unclear",
    "option2": "looks good to me",
    "option3": "Foo",
    "option4": "Bar",
    "option5": "Baz"
}

random_selection = key, val = random.choice(list(eightball_choices.items()))

print(random_selection[1])