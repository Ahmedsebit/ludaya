'''
MAC
'''

MAC = [
    {
        'name':'I experiencing the following issue with my macbook',
        'tasklist':[
            'Persistent beachball',
            'Lost a file',
            'Switching is slow',
            'Safari is slow',
            'Documents open in the wrong app',
            'Mac wont start',
            'Need to rescue my files',
            'Mac starts, but stops',
            'Kernel panic',
            'An application is playing up',
            'My hard disk is full',
            'Flash drive wont read',
            'Something just seems funny',
            'Forgotten password',
            'Screen goes weird',
            'Failed to sync',
            'Audio input/output broken',
            'Cleanup needed'
        ]
    }
]

def mac_list_length():
    l = []
    for i in MAC:
        for j in i.values()[0]:
            l.append(j)

    return l
