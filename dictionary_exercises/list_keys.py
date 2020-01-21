digitalcrafts = {
    'US': {
        'Georgia': {
            'Atlanta': '3423 Pidemont Rd NE #420',
        },
        'Texas': {
            'Houston': '3302 Canal St.'
        }
    },
    'UK': {
        'London': {
            'Camden Town': 'Camden Lock'
        }
    }
}

# LONG WAY

countries = digitalcrafts.keys()
us_cities = digitalcrafts['US'].keys()

#print(countries)
#print(us_cities)

# OR, you can iterate over the dictionary in a FOR loop

for country in digitalcrafts:
    print('There are campuses in the %s' % country)
