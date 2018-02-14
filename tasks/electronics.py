'''
Task lists
'''
ELECTRONICS = [
    {
        'name':'Direct me on how to resolve the following electrical problem I\'m experiencing:',
        'tasklist':[
            'Overlamping',
            'Uncovered Junction Box',
            'Too Few Oulets',
            'No GFCIs',
            'Overwired Panel',
            'Backstabbed Wires',
            'Ungrounded (2-prong) Receptacles',
            'Plug Falls Out of Receptacle',
            'Power sags and dips',
            'Switches of light are not working',
            'Flickering light',
            'Electric shocks',
            'No RCCB - Residual Current Circuit Breaker',
            'Frequent burning out of light bulbs',
            'Overcircuited panel',
            'High electric bill',
            'Frequent electrical surges',
            'Circuit breaker is tripping too frequently',
            'Circuit are overloading',
            'Lights are too bright or too dim',
            'Recessed light goes out and comes back on'
        ]
        }
]

def electronics_list_length():
    l = []
    for i in ELECTRONICS:
        for j in i.values()[0]:
            l.append(j)

    return l