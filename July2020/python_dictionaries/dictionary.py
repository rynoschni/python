meal = {
    "drink": "",
    "appetizer": "chips",
    "entree": "taco",
    "dessert": "churros"
}

# print("This Thursday I will have a %s and a %s for dinner" % (meal["drink"], meal["entree"]))
print(meal)

if "dessert" in meal:
    del meal["dessert"]
    print(meal)
else:
    meal["dessert"] = "churros"
    print(meal)