'''
MAC
'''

MAC = [
    {
        'name':'MAC Administration',
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
            'I cant eject a disc',
            'My hard disk is full',
            'My optical drive wont read',
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
