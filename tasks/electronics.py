'''
Task lists
'''
ELECTRONICS = [
    {
        'name':'Wires electricity',
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
            'No RCCB (Residual Current Circuit Breaker)',
            'Frequent burning out of light bulbs',
            'Overcircuited panel',
            'High electric bill',
            'FREQUENT ELECTRICAL SURGES',
            'CIRCUIT BREAKER TRIPPING FREQUENTLY',
            'CIRCUIT OVERLOAD',
            'LIGHTS TOO BRIGHT OR DIM',
            'RECESSED LIGHT GOES OUT AND COMES BACK ON'
        ]
        }
]

def electronics_list_length():
    l = []
    for i in ELECTRONICS:
        for j in i.values()[0]:
            l.append(j)

    return l