digitalcrafts = {
    'US': {
        'Georgia': {
            'Atlanta': '3423 Pidemont Rd NE #420',
        },
        'Texas': {
            'Houston': '3302 Canal St.'
        }
    }
}

for country in digitalcrafts:
    for state in digitalcrafts[country]:
        print(country, state, end=': ')
        for city in digitalcrafts[country][state]:
            print(city)
