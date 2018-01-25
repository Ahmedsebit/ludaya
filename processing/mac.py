'''
MAC
'''

MAC = [
    {
        'name':'Im experiencing the following issue with my macbook',
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
            'Forgotten password',
            'Screen goes weird',
            'Failed to sync',
            'Audio input/output broken',
            'Cleanup needed',
            'iTunes 12.5 with macOS Sierra not responding Problem',
            'macOS Sierra issues: macOS Sierra install frozen/stuck',
            'macOS Sierra update problems: macOS Sierra wont start up after update',
            'macOS Sierra problems reboot',
            'Problems with macOS Sierra: Mac apps cant be opened or damaged',
            'macOS Sierra update problems: slow macOS Sierra performance',
            'macOS Sierra upgrade issues: slow Wi- Fi',
            'Fix to Problems with macOS Sierra Playing Certain Video Formats',
            'macOS Sierra update problems: Bluetooth Not Available',
            'macOS Sierra upgrade issues & fixes: fast battery drain',
            'macOS Sierra problems and solutions: mail problem',
            'Problems with macOS Sierra upgrade: external hard drive/SD card not showing',
            'macOS Sierra update issues: freezing/crashing using Safari',
            'macOS Sierra upgrade freezing problems',
            'such as slow to start or halted startup',
            'Apple computer does not boot or start up to the desktop',
            'Cant boot the computer using external media or an optical drive',
            'Computer does not boot consistently',
            'The hard drive is unresponsive and Disk Utility needs to be run',
            'Data from a previous Apple computer needs to be transferred to a new model',
            'Apple computer needs to load a network-based image',
            'Apple computer will not boot completely',
            'Apple computer experiences unknown issues delaying boot',
            'Apple computer experiences odd behavior(s) while in use and/or during boot up',
            'The password linked to a user account on an Apple computer has been forgotten',
            'Cant boot the computer using external media or an optical drive',
            'Mac Wont Start',
            'Error Message - Downloaded .app is damaged and cant be opened',
            'VPN doesnt work',
            'WiFi Issues',
            'Remove Bluetooth',
            'Forcefully removing network configuration files',
            'Changing Router Settings / Reset Router',
            'Forgot OS X Password',
            'Can Receive But Cant Send Email Messages',
            'Constant Welcome To Mail Message',
            'Audio Not Working',
            'Printer Issues',
            'like drives not appearing',
            'Bluetooth problems',
            'AirPort non connecting',
            'Notification Issues',
            'forgets the preference settings after a reboot',
            'Improve Battery Life',
            'Sierra is Frozen/Stuck',
            'sierra frozen/stuck',
            'Cant Start Mac after Update',
            'sierra cant start',
            'iTunes Doesnt Respond',
            'Sierra Working Slow',
            'sierra working slow',
            'Apps Are Damaged'
        ]
    }
]

def mac_list_length():
    l = []
    for i in MAC:
        for j in i.values()[0]:
            l.append(j)

    return l
