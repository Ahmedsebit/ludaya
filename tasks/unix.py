'''
UNIX
'''

UNIX = [
    {
        'name':'UNIX Administration',
        'tasklist':[
            'Command not found',
            'Permission denied',
            'No route to host',
            'Connection refused',
            'Fix Linux booting problems',
            'When booting stalls',
            'Fix Linux driver problems',
            'Graphics hardware',
            'Wheres my desktop?',
            'Fix Linux wireless networking problems',
            'Double top'
        ]
    }
]

def unix_list_length():
    l = []
    for i in UNIX:
        for j in i.values()[0]:
            l.append(j)

    return l