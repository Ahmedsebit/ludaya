# coding: utf8
'''
Task lists
'''
HARDWARE = [
    {
        'name':'Experiencing the following hardware problems:',
        'tasklist':[
            {
                'taskname':'System Is Dead, No Cursor, No Beeps, No Fan',
                'taskanswer':'Power Cord Failure, Power Supply Failure, Mother Board Failure, Memory Failure Plug In or Replace Power Cord, Power Cords Can Fail Even, Though They Look Fine, Replace The Power Supply; Use a Known-good Spare For Testing, Replace Motherboard, Use a known-good spare for testing, Remove All Memory (RAM) retest. if the system still wont boot replace bank 1'
                },
            {
                'taskname':'System Beeps on start up, Fan is running, no cursor on screen',
                'taskanswer':' Improperly Seated or failing graphics adapter. Reset or replace graphics adapter, use known-good spare or testing.'
                },
            {
                'taskname':'Operating System will not boot',
                'taskanswer':'Poor Heat conduct to heat sink. Motherboard not configured properly. Software errors Check CPU heat sink/ Fan: Replace if necessary, use one with higher capacity. Set jumpers/DIP switch for proper motherboard Speed and ratio. Improper drivers or in compatible hardware: Update drivers and check for compatibility issues.'
                },
            {
                'taskname':'System looks up',
                'taskanswer':'Corroded memory sockets and modules. Remove Memory, clean sockets, clean pins in memory module.'
                },
            {
                'taskname':' Soft (random) Memory errors',
                'taskanswer':'Incorrect type or speed. Use memory that matches recommended type and speed by motherboard.'
                },
            {
                'taskname':'Continuous error beep, No display',
                'taskanswer':'Ram Card is not fix Properly. Check whether the RAM card is fixed properly. clean the slots with a soft brush, and the cards with surgical sprit, if no changes in the beep sound change the RAM card'
                },
            {
                'taskname':'The main drive is a slave but not as a master',
                'taskanswer':'Master/ Slave configuration is not configured properly. Check master/ Slave configuration (jumpers) in the drive.'
                },
            {
                'taskname':'Even after detecting hard disk, the computer is still not working and I get errors',
                'taskanswer':'Hard Drive Not Prepared Partition and format the drive. this must be done before it can be used.'
                },
            {
                'taskname':'I Have a 80gb hard drive but my system says it is around 500 MB in size',
                'taskanswer':'BIOS cannot recognize the drive capacity. Update the BIOS. To update the BIOS you can logon to the vendor·s web site and download the compatible software.'
                },
            {
                'taskname':'The Hard drive, Says C: drive failure insert boot disk',
                'taskanswer':'Damaged boot Sector. Drive is dead or dying. Boot the system from a system disk. then see if you can read anything from the hard drive. Format the hard disk with system files and restart.'
                },
            {
                'taskname':'I have no video at all',
                'taskanswer':'Monitor is malfunctioning VGA card is not seated properly in the slot. First check the monitor. is it plugged in, turned on, and the cable connected correctly. are the brightness and contrast knobs turned on full? If these two possibilities are ruled out, make the VGA card is seated correctly in the BUS. finally, install the video card in another video card and see if your monitor cranks up.'
                },
            {
                'taskname':'Slow video performance with any card type',
                'taskanswer':'Video BIOS is not cached. Enable caching of video BIOS.'
                },
            {
                'taskname':'Picture displayed in DOS, but not in windows',
                'askanswer':'Wrong video driver. Start system in safe mode, verify video driver and install the correct driver.'
                },
            {
                'taskname':'System Reboots, Power is good but voltage level is out of limit',
                'taskanswer':'Check PSU withmulti-meter. replace power supoply'
                },
            {
                'taskname':'Electrical Shocks on case',
                'taskanswer':'Power supply is not grounding properly. Change power cable to 3pin cable. check domestic wiring for faults.'
                },
            {
                'taskname':'System Cant Maintain correct date and Time when turned off',
                'taskanswer':'CMOS battery about to fail. Replace CMOS battery'
                },
            {
                'taskname':'BIOS Update fails error BIOS are not compatible',
                'taskanswer':'Enable flash recovery features and restore BIOS.'
                },
            {
                'taskname':'Key board failure error appears when starting the system',
                'taskanswer':'Keyboard not plugged in properly.'
                },
            {
                'taskname':'Keys are sticking',
                'taskanswer':'Remove key tops and clean under keys, or wash out keyboard.'
                },
            {
                'taskname':'An itching fan sound',
                'taskanswer':'Switch off and isolate the main supply. Open the cabinet cover so that your mother board is visible. Look around and find the processor on the mother board. Try to rotate the fan mounting screws in anti-clockwise direction. At certain position the screws hold tight to the processor and any loose fitting ends. Put back the cabinet cover. Connect and switch on the computer. Now you have solved an irritating sound problem!'
                },
            {
                'taskname':'Replacing system battery',
                'taskanswer':'Switch off and isolate the main supply. Open the cabinet cover so that your mother board is visible. Look around and find the system battery on the mother board. Remove the weak battery located on the motherboard. Replace the old battery with a new battery. Put back the cabinet cover. Connect and switch on the computer. Now you have solved a nagging problem!'
                },
            {
                'taskname':'Computer Freeze',
                'taskanswer':'Heat is the measure Reason for PC hardware problems. Ensure if it’s computer freeze or lockup. Generally, your computer temperature is controlled by the internal fan called the Heat Sink. Dust is another enemy of PC hardware as it sticks on motherboard and electrical components. You can control overheating by removing dust from around the internal fan'
                },
            {
                'taskname':'A blue screen with a memory reference x000xxxx as a boot interruption',
                'taskanswer':'This is due to faulty RAM chips. These Faulty RAM chips are unable to store the boot loader or NT loader file therefore the OS cannot find it and hence it shuts down all the processes, due to non-availability of the boot loader file in the RAM as a result the PC restarts again and again. This problem can be fixed by replacing the old RAM with a new one. You must know the model compatibility of you motherboard before buying a new RAM. It may be DDR, DDR2 or DDR3. Just do it!'
                },
            {
                'taskname':'Noisy Computer',
                'taskanswer':'It means that the computer system is making noise while running. The reason of Noisy Computer is Dirty Fan. The dust particles sticks on the Fan including the Heat Sink and other parts such as Motherboard and other electrical parts of computer .This dust Blocks the smooth action of Fan and causing the fan to make noise. Clean your system completely by removing motherboard from its place and also clean the Fan and Heat sink with a brush or soft cloth.'
                },
            {
                'taskname':'A rapid beep sounds but no display in my monitor',
                'taskanswer':'Dirty RAM, Loosen RAM and dusty RAM slot'
                },
            {
                'taskname':'PC doesnt boot, a beep sound and displays nothing at all',
                'taskanswer':'If you notice that your CPU fan is running but there is no display in the screen, then remove the RAM from the slot, clean it and place it back properly or try another slot.'
                },
            {
                'taskname':'No sound plus and no display',
                'taskanswer':'Dirty RAM, Loosen RAM and dusty RAM slot'
                },
            {
                'taskname':'PC restarts automatically',
                'taskanswer':'Dirty RAM, Loosen RAM, dusty RAM slot and worst the RAM itself.'
                },
            {
                'taskname':'Files taking a longer time to transfer',
                'taskanswer':'Harddrive may be going bad'
                },
            {
                'taskname':'Boot time increased significantly',
                'taskanswer':'Harddrive may be going bad'
                },
            {
                'taskname':'Clicking or loud whining noises',
                'taskanswer':'Harddrive may be going bad'
                },
            {
                'taskname':'The display seem garbled',
                'taskanswer':'Videocard may be going bad and will warrant further testing'
                },
            {
                'taskname':'Seeing artifacts on the screen that I did not see before',
                'taskanswer':'Videocard may be going bad and will warrant further testing'
                },
            {
                'taskname':'Experiencing blue screens during graphics intensive tasks',
                'taskanswer':'Videocard may be going bad and will warrant further testing'
                },
            {
                'taskname':'Screen instability during graphics intensive tasks',
                'taskanswer':'Videocard may be going bad and will warrant further testing'
                },
            {
                'taskname':'The system starts heating up immediately after being booted',
                'taskanswer':''
                },
            {
                'taskname':'Clicking noises can be heard from the hardware of the system',
                'taskanswer':'hard disk is overheated. The reason for this is lack of proper ventilation or a faulty CPU fan which overheats the system to the point that the hard disk crashes. The solution for the heating issue is to ensure that the CPU fan has been installed properly and is providing sufficient cooling to the hard disk. Moreover, you can install an application that keeps you notified about the temperature of your hard disk. If it starts exceeding the maximum limit then shut down the PC for a while and let it cool down before resuming your work.'
                },
            {
                'taskname':'Computer fails to detect hard disk',
                'taskanswer':'In such cases open your system unit, check the cable connection to your Hard disk and if you find it loses then reconnect it. Also, check Ram is placed in its correct place or not if not placed correctly then reinsert it properly. Now check the power connection to your mother board. If everything is alright then close the system unit and press the Power button. BY doing this you can fix your Hard disk problem.'
                },
            {
                'taskname':'Computer fails to detect BIOS',
                'taskanswer':' This causes the hard disk to not spin properly which causes the PC to not detect either the BIOS or the hard disk. The best possible way to solve this issue is to ensure that the power supply being used for the hardware components of the PC especially the hard disk are working properly. You can do this by changing the cable connecting the UPS to the hard disk and also by switching to a UPS of a reputable company.'
                },
            {
                'taskname':'Unexpected computer crashes',
                'taskanswer':'The reason for this mostly is the accumulation of bad sectors over a large period of time. As the bad sectors pile up, the hard disk’s spindle motor malfunctions and read/write head becomes jammed. If this happens, you start hearing grinding noises from the hard disk and files and folders suddenly start disappearing. You can solve this problem by properly maintaining your hard disk and installing anti-virus programs that keep your hard disk clean and protect it from the threat of viruses that can result in the creation of bad sectors. Moreover, replacing the hard disk after 3-4 years is also a good way to avoid this issue.'
                },
            {
                'taskname':'Printing takes too long',
                'taskanswer':' Rev up printer performance--and save ink in the process--by reducing print quality for everyday output. While printer settings vary by model. Other speedup suggestions: Print pages from websites without graphics, and add RAM to your printer'
                },
            {
                'taskname':'Printer Paper jams',
                'taskanswer':'Your User Guide or control panel instructions should walk you through this easily enough. In fact, some Xerox printers provide video assistance and lighted interiors to make jam clearance a snap. Start by inspecting the paper path and remove any jammed material, being careful to take out any stuck paper straight —and above all—not tearing it. If it’s caught between rollers, follow the guide on how to release the pressure. If it’s a misaligned paper that caused the jam, remove the tray to make sure the paper is positioned correctly and reseat the tray. Sometimes you may find no misfed sheet at all, in which case you’ll need to remove the paper stack, check to see if it’s squared properly and reposition it back in the tray—all after taking a deep breath. As a rule you should always make sure the type of paper being printed is supported by your printer. And also remember to store your paper where it’s dry to avoid moisture that can make printing difficult.'
                },
            {
                'taskname':'Really bad looking prints',
                'taskanswer':'Try these easy fixes for better quality laser printing. If your issues persist, the problem is more likely to be due to supplies or hardware. Check your print driver to make sure you have the correct paper or media selected. Double check that the paper loaded in the tray matches the type selected in the printer driver. In some laser printers, the fuser has an adjustment for paper type. If your printer’s fuser can be adjusted manually, check to see that it’s set properly but be aware: fusers get very hot so exercise caution. Check out your toner cartridges, imaging unit(s) and the fuser for damage. These components vary by model and manufacturer so it’s best to refer to the User Guide. If you’ve got smudge marks, print several blank sheets of paper and they will eventually fade away'
                },
            {
                'taskname':'My printer isn’t printing',
                'taskanswer':'First, check that you sent the print job to the right printer; you may very well be printing dozens of documents in the next department. To make your main printer your default, click navigate to Printers and Faxes in Windows®. Right-click on your printer icon and select Set as default printer. Did you check that there’s enough—and the correct kind—of paper in the tray? While you’re at it, make sure your printer is on and that all cables are secure. Both USB- and network-connected computers require that the print driver be installed on the computer you’re printing from. Print drivers with a two-way communication feature can tell you what might be causing your issue via desktop or driver notifications, without making a trip to the printer. And finally, if your printer just won’t print or your print job seems stuck in the queue, the easiest solution is to restart. Begin by restarting your software application. If that doesn’t work, reboot your computer. Lastly, turn off your printer for a few minutes before switching it back on.'
                },
            {
                'taskname':'Windows is sending print jobs to the wrong printer',
                'taskanswer':'For some mysterious reason, Windows may select a new default printer--the one it automatically sends print jobs to. (This happened to me when I upgraded from Vista to Windows 7.) To fix this glitch in Windows 7, click Start (the Windows icon in the lower-left corner of the screen) and select Devices and Printers. Under Printers and Faxes, right-click the printer you want to make the default, and select Set as default printer.'
                },
            {
                'taskname':'My prints are too light, too spotty, or have horizontal lines',
                'taskanswer':'You may have a clogged print head, a problem that can occur if you use an inkjet printer infrequently. Your printers utility program can clean out the dried ink, and print a test page for inspection. The step-by-step instructions on how to do this vary by printer. From the Windows 7 Start menu, click Devices and Printers or Control Panel, and look for your printers utility app. For additional details, read "Solve Inkjet Printer Problems." For more tips on unclogging ink nozzles, go here. (Again, these steps may vary slightly for Vista and XP users.)'
                },
            {
                'taskname':'My printer says my ink cartridge is empty. I think its lying',
                'taskanswer':'You may be right. Printer out-of-ink messages are notoriously unreliable. The good news: You can try various hacks to get around those ink cartridge controls. Were not suggesting that all, or even some, of these reader tips will work with your printer, but theyre worth a try. One tip reveals how to reset ink cartridges for various HP printers. And a video on this page shows how to revive an "out of ink" Epson cartridge. If youre feeling adventurous, check them out.'
                },

            {
                'taskname':'My wireless printer is too slow',
                'taskanswer':'To get the best performance from a network printer, it is hard to beat a wired, Ethernet-cable-to-router connection. Wireless printing may be more convenient in many homes and offices, but it has its limitations. Since Wi-Fi speeds slow down with distance, Place your wireless printer as close as possible to the router. Also, make sure your Wi-Fi printer or any wireless print server it connects to supports the 802.11n spec, which can rival the performance of 100-mbps Ethernet.'
                },
            {
                'taskname':'I use remanufactured or refilled ink cartridges, and my prints look awful',
                'taskanswer':'We recommend sticking with the manufacturers ink. Third-party products may save you money up front, but the consequences can get ugly--literally--if the cheaper inks produce lower-quality prints.'
                },
            {
                'taskname':'I dont know how to fit more text on one page. How do I do it?',
                'taskanswer':'Shrinking text to fit two pages on one sheet saves money (buy less paper) and speeds up printing (fewer pages to print). This two-for-one approach is best for spreadsheets, receipts, and other documents that are still legible once shrunken. In any Windows program, select Print and Properties, and then look for a printer setting that lets you increase the number of pages per sheet.'
                },
            {
                'taskname':'Projector colours distorted on the image',
                'taskanswer':'There are a few reasons why this may be occuring, the first thing to check first is your projector cables, the best thing to do first is to change these to see if this fixes the problem. If not, the problem may lie with your colour wheel / main board.'
                },

            {
                'taskname':'Lines / Dots on the image',
                'taskanswer':'This is a problem caused by the projectors main board. When there is a problem with the main board, it may be worth considering comparing the cost of getting a completely new projector rather than buying the main board.'
                },
            {
                'taskname':'Projector overheating',
                'taskanswer':'This is quite a common case & is quite distinctive. It is usually caused by a problem with the fan. If there is no noise then that means the fan will not be working any more to help cool down your projector. Other things to look out for are making sure that you aren’t leaving your projector in very bright direct sunlight as this obviously won’t help the projector cool down.'
                },

            {
                'taskname':'Projector turning on then off straight away',
                'taskanswer':'There are a number things to look out for. The first thing to check is your power supply and make sure that all of your cables are in fully working condition and connected properly. After that, it would be worth checking how dusty the projector is, this may occur after a long period of time. This would mean having to service your projector.'
                },
            {
                'taskname':'Projector on but no image',
                'taskanswer':'If you can get your projector to turn on but then get no image, make sure that the cables that you are connecting with are connected correctly. If this is all OK, then it most likely you have a problem with your lamp ballast unit or the lamp itself. The lamp ballast unit is what provides power to the lamp. If the lamp ballast unit goes, then most likely the lamp will usually go as well. Price varies on these units so your projector would have to be taken in for an assessment.'
                },

            {
                'taskname':'Projector has shadows appearing on the image',
                'taskanswer':'This problem only applies to DLP Projectors. This yet again could be a problem with the projector’s main board or it could be a problem with the mirror. The projector would need to be assessed to find the full extent of your problem. A mirror for your projector would be a reasonably cheap repair but again with the main board if that is the problem, it would be worth considering buying a new projector.'
                },
            {
                'taskname':'Projector has dull image being produced',
                'taskanswer':'This problem only applies to LCD Projectors. All projector lamps will have a certain lamp life varying from model to model. If the image is starting to get more dull, it would be worth thinking about getting a new bulb. Some projectors will tell you how many lamp hours have been used to date, if not you may have to have a think and estimate how long you’ve been using the projector for. If you think it is near the estimated lamp life of the projector, then it may be time to enquire about buying a new projector bulb.'
                },
            {
                'taskname':'Projector inputs not working',
                'taskanswer':'If your inputs are not working on your projector then if after you’ve double checked your inputs are connected correctly, this problem is related again to the main board. For a definite price on the real cost of this, you would need to get it assessed by a projector repair centre. For Just Projectors repairs department.'
                },
            {
                'taskname':'Projector has colour around the edge of the image',
                'taskanswer':'This may occur on LCD projectors if the LCD prism becomes faulty. An LCD Prism is an expensive component on a projector and should only be thought about if absolutely necessary, in most cases it may just be best to look at buying a new projector.'
                },
        ]
    },
]

def hardware_list_length():
    l = []
    for i in HARDWARE:
        for j in i.values()[0]:
            l.append(j)

    return l