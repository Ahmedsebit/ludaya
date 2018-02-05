'''
MAC
'''

MAC = [
    {
        'name':'Im experiencing the following issue with my macbook',
        'tasklist':[
            {
                'taskname':'Persistent beachball',
                'taskanswer':''
                },
            {
                'taskname':'Lost a file',
                'taskanswer':''
                },
            {
                'taskname':'Switching is slow',
                'taskanswer':''
                },
            {
                'taskname':'Safari is slow'
                },
            {'taskname':'Documents open in the wrong app'},
            {'taskname':'Mac wont start'},
            {'taskname':'Need to rescue my files'},
            {'taskname':'Mac starts, but stops'},
            {'taskname':'Kernel panic'},
            {'taskname':'An application is playing up'},
            {'taskname':'My hard disk is full'},
            {'taskname':'Flash drive wont read'},
            {'taskname':'Forgotten password'},
            {'taskname':'Screen goes weird'},
            {'taskname':'Failed to sync'},
            {'taskname':'Audio input/output broken'},
            {'taskname':'Cleanup needed'},
            {'taskname':'iTunes 12.5 with macOS Sierra not responding Problem'},
            {'taskname':'macOS Sierra issues: macOS Sierra install frozen/stuck'},
            {'taskname':'macOS Sierra update problems: macOS Sierra wont start up after update'},
            {'taskname':'macOS Sierra problems reboot'},
            {'taskname':'Problems with macOS Sierra: Mac apps cant be opened or damaged'},
            {'taskname':'macOS Sierra update problems: slow macOS Sierra performance'},
            {'taskname':'macOS Sierra upgrade issues: slow Wi- Fi'},
            {'taskname':'Fix to Problems with macOS Sierra Playing Certain Video Formats'},
            {'taskname':'macOS Sierra update problems: Bluetooth Not Available'},
            {'taskname':'macOS Sierra upgrade issues & fixes: fast battery drain'},
            {'taskname':'macOS Sierra problems and solutions: mail problem'},
            {'taskname':'Problems with macOS Sierra upgrade: external hard drive/SD card not showing'},
            {'taskname':'macOS Sierra update issues: freezing/crashing using Safari'},
            {'taskname':'macOS Sierra upgrade freezing problems'},
            {'taskname':'such as slow to start or halted startup'},
            {'taskname':'Apple computer does not boot or start up to the desktop'},
            {'taskname':'Cant boot the computer using external media or an optical drive'},
            {'taskname':'Computer does not boot consistently'},
            {'taskname':'The hard drive is unresponsive and Disk Utility needs to be run'},
            {'taskname':'Data from a previous Apple computer needs to be transferred to a new model'},
            {'taskname':'Apple computer needs to load a network-based image'},
            {'taskname':'Apple computer will not boot completely'},
            {'taskname':'Apple computer experiences unknown issues delaying boot'},
            {'taskname':'Apple computer experiences odd behavior(s) while in use and/or during boot up'},
            {'taskname':'The password linked to a user account on an Apple computer has been forgotten'},
            {'taskname':'Cant boot the computer using external media or an optical drive'},
            {'taskname':'Mac Wont Start'},
            {'taskname':'Error Message - Downloaded .app is damaged and cant be opened'},
            {'taskname':'VPN doesnt work'},
            {'taskname':'WiFi Issues'},
            {'taskname':'Remove Bluetooth'},
            {'taskname':'Forcefully removing network configuration files'},
            {'taskname':'Changing Router Settings / Reset Router'},
            {'taskname':'Forgot OS X Password'},
            {'taskname':'Can Receive But Cant Send Email Messages'},
            {'taskname':'Constant Welcome To Mail Message'},
            {'taskname':'Audio Not Working'},
            {'taskname':'Printer Issues'},
            {'taskname':'like drives not appearing'},
            {'taskname':'Bluetooth problems'},
            {'taskname':'AirPort non connecting'},
            {'taskname':'Notification Issues'},
            {'taskname':'forgets the preference settings after a reboot'},
            {'taskname':'Improve Battery Life'},
            {'taskname':'Sierra is Frozen/Stuck'},
            {'taskname':'sierra frozen/stuck'},
            {'taskname':'Cant Start Mac after Update'},
            {'taskname':'sierra cant start'},
            {'taskname':'iTunes Doesnt Respond'},
            {'taskname':'sierra working slow'},
            {'taskname':'Apps Are Damaged'}
        ]
    }
]

def mac_list_length():
    l = []
    for i in MAC:
        for j in i.values()[0]:
            l.append(j)

    return l
