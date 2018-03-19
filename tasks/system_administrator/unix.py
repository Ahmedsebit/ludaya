# coding: utf8
'''
UNIX
'''

UNIX = [
    {
        'name':'Direct me on how to resolve the following UNIX Administration issue:',
        'tasklist':[
            'Command not found',
            'Permission denied',
            'No route to host',
            'Connection refused',
            'Fix Linux booting problems',
            'When booting stalls',
            'Fix Linux driver problems',
            'Fix Linux wireless networking problems',
            'Open a command prompt when issuing a command',
            'Find out how much memory Linux is using',
            'Change permissions under Linux',
            'Access partitions under Linux',
            'Switch from one desktop environment to another, such as switching from KDE to Gnome',
            'Terminate an ongoing process',
            'Insert comments in the command line prompt',
            'Write a command that will look for files with an extension “c”, and has the occurrence of the string “apple” in it',
            'Write a command that will display all .txt files, including its individual permission',
            'Append one file to another in  Linux',
            'Find a file  using Terminal',
            'Create a folder using Terminal',
            'View the text file using Terminal',
            'Enable curl on Ubuntu LAMP stack',
            'Enable root loging in Ubuntu',
            'Run an Linux program in the background simultaneously when you start your Linux Server',
            'Uninstall the libraries in Linux',
            'How can I speed up performance by using multiple swap partitions',
            'How can I create multiple swap partitions on one or more drives',
            'How do I create a swap file in an existing Linux data partition',
            'How do I get Netscape for Linux to recognize my Netscape for Windows bookmark file',
            'How do I get my “winmodem” to work with Linux',
            'How can I tell how much memory Linux is using',
            'If Linux is not using all the memory I have installed, how do I make it use the rest',
            'How do I kill a program that has locked up',
            'I have both KDE and Gnome installed. How do I switch between them',
            'How can I add programs to the Panel',
            'How can I change my desktop background color',
            'If I want to issue a command, how do I open a command prompt',
            'How do I get help for command parameters',
            'How do I repeat a command',
            'Long pathnames are a pain to type in. Is there any sort of shortcut I can use',
            'Is there a way to use one command to start more than one program at a time',
            'Is there a way to stack commands and have them execute concurrently in other command',
            'I can’t seem to log in, even though I’m using the correct password. What’s wrong',
            'I clicked on Logout and now the session is locked up. How do I log out',
            'How can I enable Linux to automatically restart applications that are running when I use',
            'Can I use wildcard searches with the ls command, as I can with Dir in DOS/Windows',
            'I want to do a wildcard search on files with ? or * in the names. How do I do that',
            'How do I create or rename a file with special characters in the name',
            'How do I create links',
            'How do I add users',
            'How do I delete users',
            'How do I add or change personal information in an account',
            'How do I add groups',
            'How do I add/delete users in a group',
            'How do I change a password',
            'How do I display the permissions for a file or directory',
            'How do I change permissions'
        ]
    }
]

def unix_list_length():
    l = []
    for i in UNIX:
        for j in i.values()[0]:
            l.append(j)

    return l

