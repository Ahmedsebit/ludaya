'''
Task lists
'''
LEARNING = [
    {
        'name':'Updated on the latest computer periphery',
        'tasklist':[
            'test'
        ]
        },
    {
        'name':'Read trade magazines',
        'tasklist':[
            'test'
        ]
        },
    {
        'name':'Read technical manuals',
        'tasklist':[
            'test'
        ]
        },
    {
        'name':'Attend conferences on hardware',
        'tasklist':[
            'test'
        ]
        },
    {
        'name':'Attend conferences on software',
        'tasklist':[
            'test'
        ]
        }
]

def learning_list_length():
    l = []
    for i in LEARNING:
        for j in i.values()[0]:
            l.append(j)

    return l