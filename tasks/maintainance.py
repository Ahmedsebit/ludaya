# coding: utf8
'''
Task lists
'''
MAINTAINANCE = [
    {
        'name':'Maintaining computer systems',
        'tasklist':[
            'Deleting Temporary Files',
            'Scandisk',
            'Antivirus',
            'Backup',
            'Clean Up',
            'Defragment',
            'Clean Junk Files & Folders',
            'Guard against malware',
        ]
        },
    {
        'name':'Maintaining networks',
        'tasklist':[
            'Tuning the network',
            'Optimizing the network',
            'Documenting the network',
            'Securing the network from internal threats',
            'Securing the network from external threats',
            'Planning for network upgrades',
            'Planning for network expansions',
            'Planning for network enhancements',
            'Scheduling backups and restoring services or the network from backups',
            'Ensuring compliance with legal regulations and corporate policies',
            'Updating device configurations',
        ]
        },
    {
        'name':'How do I set up the following hardware',
        'tasklist':[
            'Input Devices',
            'mice',
            'keyboards',
            'trackballs',
            'graphics tablets',
            'infra-red remote controls',
            'external microphone',
            'connect via a USB cable or dongle or via the Bluetooth wireless technology',
            'Audio Devices',
            'speakers',
            'headset',
            'Display Devices',
            'monitor',
            'projectors',
            'to run two monitors if required',
            'High-Definition Multimedia Interface (HDMI)',
            'Printers',
            'Scanners',
            'Other Peripherals',
            'webcams',
            'USB hubs',
            'Memory card readers',
            'CD/DVD ROM Drives',
            'Hard drive',
            'Memory/RAM',
            'Memory Stick',
            'Modems',
            'Network Card',
            'UPS(Uninterruptible Power Supply)',
            'Video/Graphic Cards',
        ]
        },
    {
        'name':'Install software',
        'tasklist':[
            'windows',
            'mac',
            'unix',
            'dual boot',
            'office'
        ]
        },
    {
        'name':'Install drivers',
        'tasklist':[
            'Audio',
            'BIOS',
            'Change Management Software Development Kit',
            'Chipset',
            'Diagnostics',
            'Drivers for OS Deployment',
            'Modem/Communications',
            'Mouse Keyboard & Input Devices',
            'Network',
            'Removable Storage',
            'Security',
            'Serial ATA',
            'Video'
        ]
        },
    {
        'name':'Configure drivers',
        'tasklist':[
            'Audio',
            'BIOS',
            'Change Management Software Development Kit',
            'Chipset',
            'Diagnostics',
            'Drivers for OS Deployment',
            'Modem/Communications',
            'Mouse Keyboard & Input Devices',
            'Network',
            'Removable Storage',
            'Security',
            'Serial ATA',
            'Video'
        ]
        },
]

def maintainance_list_length():
    l = []
    for i in MAINTAINANCE:
        for j in i.values()[0]:
            l.append(j)

    return l