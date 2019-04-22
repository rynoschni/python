from characters import characters
from houses import houses
from pprint import pprint
# import requests # makes API requests (this is a third-party module)
# import json # convert the API data into python dictionaries and arrays
# import time # module for working with timestamps

# count the number of people who are part of a house
def make_house_histogram(character_list):
    histogram = {}

    # do the thing!
    # loop through all the characters
    for person in character_list:

        # what do I check for each person?
        allegiances = person['allegiances']
        # allegiances is a list of URLs!
        # they look like this:
        # ["https://www.anapioficeandfire.com/api/houses/77"]
        for house in allegiances:
            # do something with that house
            if house in histogram:
                histogram[house] = histogram[house] + 1
            else:
                histogram[house] = 1

    return histogram

def allegiances_histogram(character_list):
    house_dict = {}
    allegiances = []
    for c in character_list:
        if c["allegiances"]:
            for a in c["allegiances"]:
                house_name = houses[a]
                if house_name not in house_dict.keys():
                    house_dict[house_name] = 1
                elif house_name in house_dict.keys():
                    house_dict[house_name] += 1

    for h in house_dict.keys():
        allegiances.append('%s : %s' % (h, house_dict[h]))
    return allegiances

ugly_histogram = make_house_histogram(characters)
pretty_histogram = allegiances_histogram(characters)

## pprint(ugly_histogram)
pprint(pretty_histogram)
