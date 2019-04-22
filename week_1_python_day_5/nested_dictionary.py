digitalcrafts = {
    'US': {
        'Georgia': {
            'Atlanta': '3423 Pidemont Rd NE #415',
        },
        'Texas': {
            'Houston': '3302 Canal St.'
        }
    }
}

# Add a new campus
digitalcrafts['US']['Florida'] = {
    'Orlando': 'Communicore Epcot'
}

print(digitalcrafts['US'])
# print(digitalcrafts['US']['Georgia']['Atlanta'])
