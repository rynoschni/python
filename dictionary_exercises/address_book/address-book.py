# Dictionaries
# a.k.a. Hash, HashMap, HashTables, Map, Object

places = {
    'farm burger': '1234 piedmont, atlanta',
    'naan stop': '1235 piedmont, atlanta'
}

# what is the address of farm burger?
# places['farm burger']
# go get me the thing with 'farm burger' on the left hand side of the colon

friends = {
    'Europe': {
        'paris': ['frankie', 'grace'],
        'berlin': ['bobbie']
    },
    'Asia': ['my cousin', 'my other cousin', 'their friend'],
    'US': {
        'angela': {
            'pets': {
                'oakley': {
                    'toys': [
                        'everything',
                        'your stuff',
                        'strings'
                    ]
                },
                'milla': {
                    'hobbies': [
                        'drooling'
                    ]
                }
            }
        }
    }
}

# how do access the list of
# oakley's toys?

# toys = friends['US']['angela']['pets']['oakley']['toys']
# print(toys)
# for item in toys:
#    print('%s is one of oakley\'s fav toys' % (item,))
