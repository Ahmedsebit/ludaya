'''
Task lists
'''
ELECTRONICS = [

    {
        'name':'Experiencing the following electrical problem, kindly assist',
        'tasklist':[
            {
                'taskname':'Overlamping',
                'taskanswer':'Stay within the wattage limit listed on all light fixtures made since 1985. For older, unmarked fixtures, use only 60-watt bulbs or smaller.'
                },
            {
                'taskname':'Uncovered Junction Box',
                'taskanswer':'Buy a new cover and install it with the screws provided.'
                },
            {
                'taskname':'Too Few Oulets',
                'taskanswer':'Nowadays most of the houses have extension cords and power strips to rely heavily on them. If you don’t use heavy load extension cords like 14-gauge or thicker the risk will be minimal. Thus it is advisable to use more outlets with the help of an electrician.'
                },
            {
                'taskname':'No GFCIs',
                'taskanswer':'Replace old receptacles with GFCIs (about $12 each). s an alternative, GFCI breakers ($25) can be installed on the main panel. But then every time one trips, you have to go down to the basement to reset it.'
                },
            {
                'taskname':'Overwired Panel',
                'taskanswer':'Add a subpanel with a few extra slots ($250), or, if youre planning major home improvements, replace the existing panel with a larger model ($500 to $800).'
                },
            {
                'taskname':'Aluminum Wiring',
                'taskanswer':'Retrofitting a dielectric wire nut for aluminum wire to copper connection in case of light fixtures. This helps in stopping corrosion due to the grease in the nuts.'
                },
            {
                'taskname':'Backstabbed Wires',
                'taskanswer':'Check if your wires are backstabbed, if so, release it and fix them to the respective screw terminals on the receptacle.'
                },
            {
                'taskname':'Ungrounded (2-prong) Receptacles',
                'taskanswer':'Replace the old receptacles as soon as possible'
                },
            {
                'taskname':'Power sags and dips',
                'taskanswer':'Sags are dips usually occur when the power grip is faulty and electrical appliances are connected to it. It also occurs when the grid is made of low quality materials. When this is the case, it draws more power when switched on.'
                },
            {
                'taskname':'Switches of light not working',
                'taskanswer':'You can easily point out if it a bad workmanship or sub-standard products with dim switches that don’t work on adjusting the lights properly. It can also be the fault of wiring or circuit or outlet. You can consult an electrician for this issue.'
                },
            {
                'taskname':'Flickering light',
                'taskanswer':'Immediately call the electrician to get weatherhead replaced.'
                },
            {
                'taskname':'Tripping circuit breaker',
                'taskanswer':'Tripping is actually a sign that your home is protected. Just check what causes tripping and try using a low setting and also usage can be limited to a single circuit too.'
                },
            {
                'taskname':'Electric shocks',
                'taskanswer':'An electric shock happens when you switch on or off a device. The issue can either be with the appliance or the wiring. To check the issue, you can test with another device. But to be on the safer side, just talk with your electrician to resolve the issues.'
                },
            {
                'taskname':'No RCCB - Residual Current Circuit Breaker',
                'taskanswer':'This is used to disconnect the load from main supply when the circuit has residual current. By using RCCB you can ensure protection against direct and indirect contact, electric fire and protection of earthing against corrosion.'
                },
            {
                'taskname':'Frequent burning out of light bulbs',
                'taskanswer':'If your light bulbs burn out too often, check if your issue falls under this:➤ High wattage➤ Insulation is near to light➤ Poor wiring on circuit and mains, More wattage on a dimmer switch'
                },
            {
                'taskname':'Overcircuited panel',
                'taskanswer':'The difference between double-pole breakers and tandem breakers are that the latter one doesn’t take up two slots in a single circuit. The danger level will be minimal. This problem can be resolved by adding a sub-panel with extra slots or replacing the existing panel with a bigger model.'
                },
            {
                'taskname':'High electric bill',
                'taskanswer':'You can reduce electric bills by:➤ Repairing damaged circuits or wiring➤ Unplugging electronic devices when not in use➤ Relying on a cost-effective service provider➤ Recognizing power surging devices'
                },
            {
                'taskname':'Frequent electrical surges',
                'taskanswer':'It can be occurred due to poor wiring in the house or lightning strikes or faulty appliances or damaged power lines. Surges are common and last for a microsecond but if you experience frequent surges lead to equipment damage that degrade life expectancy particularly. Check the device that connects to the home grid or the wiring and try disconnecting the poor quality powerboards or devices from the outlet. If the surges don’t occur again, your problem is solved. If it is not, you must call an electrician.'
                },
            {
                'taskname':'Circuit breaker tripping frequently',
                'taskanswer':'A circuit breaker is designed to protect you and your home, so when it does trip, that’s a sign it’s doing its job. Limit the electrical usage on a single circuit while high watt devices are in use.'
                },
            {
                'taskname':'Circuit overloading',
                'taskanswer':'It is always better to fit a bulb or any other fittings by staying within the wattage. If the fixtures are not marked with wattage, it is advisable to use a 60-watt bulb or even smaller ones.'
                },
            {
                'taskname':'Lights are too bright or too dim',
                'taskanswer':'There’s two probable causes: Different types of lights with different wattage: Check that all the globes are identical. Bad main neutral connection: This will continue to cause problems for the home until it is fixed by a professional.'
                },
            {
                'taskname':'Recessed light goes out and comes back on',
                'taskanswer':'Recessed lighting are equipped with safety devices that cut out power to the light when it gets too hot. You’re either using too high wattage on the bulb, or insulation in the ceiling is too close to the bulb.'
                }
        ]
        }
]

def electronics_list_length():
    l = []
    for i in ELECTRONICS:
        for j in i.values()[0]:
            l.append(j)

    return l