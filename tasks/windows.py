# coding: utf8
'''
WINDOWS
'''

WINDOWS = [
    {
        'name':'Direct me on how to resolve or do the following WINDOWS task',
        'tasklist':[
            'Activating Windows 10',
            'Avoiding inconvenient software update reboots',
            'Updating old software to work with Windows 10',
            'Changing privacy and Wi-Fi Sense settings',
            'Printer compatibility',
            'Changing the browser to Chrome or Firefox',
            'Learning to use Edge',
            'Edge wont stream music when minimised',
            'Finding Safe Mode',
            'Making sure Windows 10 knows where you are',
            'Speeding up your PC',
            'Removing the annoying lock screen',
            'Making DVDs work again',
            'Banish annoying notifications',
            'Setting up Windows Hello',
            'Stopping Windows 10 from using loads of data',
            'Getting Cortana to respond to one voice',
            'Getting Windows 10 working on high-res screens',
            'Using less battery on laptops and tablets',
            'Generating a battery report',
            'Changing default app choices',
            'Opening older Microsoft Office files',
            'Flickering screen issues',
            'Fixing the Start menu',
            'Staying safe with the Windows Store',
            'Setting app permissions',
            'Using Windows 10 across multiple devices',
            'Fixing problems with Bluetooth connectivity',
            'Backing up a Windows 10 PC',
            'Fixing black screen errors',
            'Protecting your PC with Windows Firewall',
            'Benefiting from Windows Defender',
            'Setting up device encryption',
            'Solving sound problems',
            'Fixing the Blue Screen of Death',
            'Avoid losing files - make a backup',
            'Computer booting very slowly',
            'Tracking down resource hogging apps',
            'Avoid endless clicking of minimise',
            'Getting rid of Live Tiles',
            'Getting help from accessibility tools',
            'Problems with linking up an Xbox',
            'Use Quick Access to speed navigation up',
            'Get even faster by using keyboard shortcuts',
            'Taking a grab of a smaller section of screen',
            'Setting up Windows 10 to protect your kids',
            'Making the Start menu smaller (or bigger)',
            'Revert to previous versions of files',
            'Change Edge downloads to a different location',
            'Set auto login to avoid typing in passwords endlessly',
            'Disable lock screen adverts to speed up your machine',
            'Wi-Fi networks not showing up',
            'Removing Cortana’s big search box',
            'Moving apps to a different drive',
            'Finding files with tags',
            'Restart Windows Explorer to combat sluggishness',
            'Install apps you’ve downloaded from the web',
            'Using Windows 10 gestures to work quickly',
            'Office seemingly disappearing with Windows 10',
            'Disable annoying system sounds',
            'Kill background apps to speed your PC',
            'Sync folders with OneDrive to save space',
            'Troubleshooting via video',
            'Tweaking Control Panel to fix common problems',
            'Save to PDF so everyone can open files',
            'Hover don’t click',
            'Changing the default apps files open with',
            'Saving out a web page with Edge',
            'Fix enlarged desktop icons',
            'Decluttering the taskbar',
            'Xbox Live app login problems',
            'Keeping Cortana off the lock screen',
        ]
    }
]

def windows_list_length():
    l = []
    for i in WINDOWS:
        for j in i.values()[0]:
            l.append(j)

    return l