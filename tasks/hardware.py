# coding: utf8
'''
Task lists
'''
HARDWARE = [
    {
        'name':'Experiencing the following hardware problems:',
        'tasklist':[
            'System Is Dead, No Cursor, No Beeps, No Fan',
            'System Beeps on start up, Fan is running, no cursor on screen',
            'Operating System will not boot',
            'System looks up',
            'Continuous error beep, No display',
            'The main drive is a slave but not as a master',
            'Even after detecting hard disk, the computer is still not working and I get errors',
            'I Have a 80gb hard drive but my system says it is around 500 MB in size',
            'The Hard drive, Says C: drive failure insert boot disk',
            'I have no video at all',
            'Slow video performance with any card type',
            'Picture displayed in DOS, but not in windows.',
            'System Reboots, Power is good but voltage level is out of limit',
            'Electrical Shocks on case.',
            'System Cant Maintain correct date and Time when turned off',
            'BIOS Update fails error BIOS are not compatible',
            'Key board failure error appears when starting the system',
            'Keys are sticking'
            'A blue screen that started happening in one good cold morning',
            'An itching fan sound',
            'Replacing system battery',
            'Computer Freeze',
            'A blue screen with a memory reference x000xxxx as a boot interruption',
            'Laptops dead',
            'Noisy Computer',
            'A rapid beep sounds but no display in my monitor',
            'PC doesnt boot, a beep sound and displays nothing at all.',
            'No sound plus and no display?',
            'PC turns on, no sound and display.',
            'When I install a software an error pops-up?',
            'When installing a software suddenly it stops and cannot continue.',
            'PC restarts automatically?',
            'Files taking a longer time to transfer',
            'Boot time increased significantly',
            'Clicking or loud whining noises',
            'The display seem garbled',
            'Seeing artifacts on the screen that I did not see before?',
            'Experiencing blue screens during graphics intensive tasks',
            'Screen instability during graphics intensive tasks?',
            'The system starts heating up immediately after being booted.',
            'Clicking noises can be heard from the hardware of the system',
            'Computer fails to detect hard disk',
            'Computer fails to detect BIOS',
            'Unexpected computer crashes',
            'Printing takes too long',
            'Printer Paper jams',
            'Really bad looking prints',
            'My printer isn’t printing',
            'Windows is sending print jobs to the wrong printer',
            'My prints are too light, too spotty, or have horizontal lines',
            'My printer says my ink cartridge is empty. I think its lying',
            'My wireless printer is too slow',
            'I use remanufactured or refilled ink cartridges, and my prints look awful',
            'I dont know how to fit more text on one page. How do I do it?',
            'I cant print from my mobile device to my printer',
            'My MFP wont scan anymore',
            'Colours distorted on the image',
            'Lines / Dots on the image',
            'Projector overheating',
            'Projector turning on then off straight away',
            'Projector on but no image',
            'Projector has shadows appearing on the image',
            'Projector has dull image being produced',
            'Projector inputs not working',
            'Projector has colour around the edge of the image',
            'Projector has lamp door switch broken'
        ]
    },
    {
        'name':'Kindly prepare evaluations for this hardware',
        'tasklist':[
            'tape drives - LTO-5 Tape Drive - LTO Ultrium 5 - 3 Tb',
            'microphones Blueair - Snowball iCE USB Cardioid Condenser Microphone',
            'loudspeakers - Logitech Z906 5.1',
            'headphones - Mpow 059 Bluetooth Headphones Over Ear',
            'graphic tablets - XP-Pen Artist16 15.6 Inch IPS Drawing Monitor Pen Display Drawing Tablet',
            'touchscreens - Microsoft Surface Studio',
            'barcode readers - TaoTronics USB Barcode Scanner ',
            'printers - HP PageWide Pro 477dw',
            'projectors - Epson EX7240 Pro WXGA 3LCD Projector Pro',
            'Mouse- Logitech MX Master 2S Wireless Mouse with Cross-Computer Control',
            'Keyboard - Logitech - MK320 Wireless Keyboard',
            'CD Rom - Apple - SuperDrive 8x External USB Double-Layer DVD±RW/CD-RW Drive - Silver',
            'Scanner - Epson FastFoto FF-640',
            'CPU - Dell New Precision 5720 All-in-One',
            'CPU - Dell New XPS Tower Special Edition',
            'CPU - HP Z2 Mini G3 Workstation',
            'MAC -  Retina 4K Display 3.0GHz Processor 1TB Storage',
            'Laptop - HP SPECTRE X360',
            'Laptop - Dell XPS 13 Laptop',
            'Laptop - ASUS Chromebook Flip C302 with Intel Core m3',
            'Laptop - MACBOOK PRO (13 INCH, NO TOUCHBAR) 2017',
            'webcam - Logitech - C920 Pro Webcam - Black'
        ]
        }
]

def hardware_list_length():
    l = []
    for i in HARDWARE:
        for j in i.values()[0]:
            l.append(j)

    return l