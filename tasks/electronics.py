'''
Task lists
'''
ELECTRONICS = [
    {
        'name':'Experiencing the following electrical problem, kindly assist',
        'tasklist':[
            'Overlamping',
            'Uncovered Junction Box',
            'Too Few Oulets',
            'No GFCIs',
            'Overwired Panel',
            'Aluminum Wiring',
            'Backstabbed Wires',
            'Ungrounded (2-prong) Receptacles',
            'Plug Falls Out of Receptacle',
            'Power sags and dips',
            'Switches of light not working',
            'Flickering light',
            'Tripping circuit breaker',
            'Electric shocks',
            'No RCCB - Residual Current Circuit Breaker',
            'Frequent burning out of light bulbs',
            'Overcircuited panel',
            'High electric bill',
            'Frequent electrical surges',
            'Circuit breaker tripping frequently',
            'Circuit overloading',
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