# coding: utf8
'''
Task lists
'''
SUPPORT = [
    {
        'name':'Direct me on how to do the following Wave task',
        'tasklist':[
            'Add Employees',
            'Complete your Tax Profile',
            'Enter Payroll History',
            'Direct Deposit Application',
            'Enter Employee Hours',
            'Pay Your Employees!',
            'Receiving Your First Payment',
            'Receiving Deposit',
            'Receiving Deposits',
            'Changing Deposit Account',
            'Reconciling Invoices',
            'Pausing Payments by Wave',
            'Protecting your Business - Card Merchant Best Practices',
            ]
        },{
        'name':'Direct me on how to do the following Zoho CRM task',
        'tasklist':[
            'Add a Facebook Page',
            'Add a Twitter Handle',
            'Add a Google+ Page',
            'Remove Twitter/Facebook/Google+ Company Profile',
            'Enable Social Admin Permission',
            'Add a Lead/Contact from Facebook/Twitter/Google+',
            'Automate lead generation via social media',
            'Check the Activity Stream',
            'Add Keyword Tracking and Custom Streams for Twitter',
            'View Social Interactions',
            'Generate Web Forms',
            'Create Auto Response Rule',
            'Create Auto Response Rule Entry',
            'Enable Email Insights',
            'Monitor email response contextually',
            'How Zoho CRM tracks email activity',
            'Sort records by email status',
            'View email reports',
            'Email analytics',
            'Email and call analytics',
            'Sent Email status',
            'View email and call analytics',
            'Track email template performance',
            'Configure Gamescope Settings',
            'Filter records using advanced filters',
            'Use advanced filters effectively',
            'Filter records using Visitor Tracking information',
            'Enable CalDAV Access in Zoho CRM',
            'Configure CalDAV Account in an iOS Device',
            'Delete CalDAV Account',
            'View Trend Dashboards in Zoho CRM',
            'View Zia Notifications in Zoho CRM',
            ]
        },{
        'name':'Direct me on how to do the following MailChimp task',
        'tasklist':[
            'Set Up my Account',
            'Work With my List',
            'Customize my Signup Form',
            'Create a Campaign',
            'View my Campaign Reports',
            'Review Optional Advanced Features',
            ]
        },{
        'name':'Direct me on how to do the following Dropbox task',
        'tasklist':[
            'File backup and management-Dropbox',
            'Create private folder',
            'Create shared folder',
            'Track team activity',
            'Overseeing team activity',
            'Create full report',
            'Link a team member third-party app to their Dropbox account',
            'Link a team member computer to their Dropbox account',
            'Link a team member mobile device to their Dropbox account',
            'Add member to the team',
            'Removed member from the team',
            'Monitormy entire team by viewing specific events',
            'Creating full reports across specific dates',
            'Add more licenses to my plan',
            'View my current plan',
            'Update billing information',
            'Review billing history.',
            'Collaborate with the Dropbox Badge',
            'Joining a team',
            'Add comments on files',
            'Restoring a deleted file',
            'Add an extra layer of security',
            'To see how much space my entire team has used',
            'Adding computers to Dropbox',
            'File Revisions',
            'Account transfer',
            'Migrate data from a server',
            'Add your team files',
            'Set up my team folders',
            'Add tiered admins',
            'Invite your team',
            'Permanent file deletions',
            'Configure single sign-on',
            'Remote wipe',
            'Configure sharing settings',
            'Set folder permissions',
            ]
        },{
        'name':'Direct me on how to do the following Skype task:',
        'tasklist':[
            'Online meetings-Skype',
            'Add a contact in Skype for Business',
            'Send an IM in Skype for Business',
            'Set up a Skype for Business meeting in Outlook',
            'Share your desktop or a program in Skype for Business',
            'Make and receive calls using Skype for Business',
            'Make and receive a Skype for Business video call',
            'Add a contact in Skype for Business',
            'Set up audio in Skype for Business',
            'Set up video in Skype for Business',
            'Make a call in Skype for Business',
            'Schedule a Skype for Business Meeting',
            'Join a Skype for Business Meeting',
            'Meet and share using Skype for Business',
            'Presence and IM in Skype for Business',
            ]
        },{
        'name':'Direct me on how to do the following AkrutoSync task:',
        'tasklist':[
            'Outlook sync-AkrutoSync',
            'Configuring AkrutoSync to sync with your phone',
            'Configuring AkrutoSync to sync over the Internet',
            'Obtaining a DNS name from a third-party service No-IP.com',
            'Obtaining a DNS name from a third-party service DNSDynamic',
            'Obtaining a DNS name from a third-party service Two-DNS.de',
            'Other options for obtaining a DNS name other than from a third party',
            'Completing AkrutoSync setup to sync over the Internet',
            'Configuring AkrutoSync to sync over your home Wi-Fi network',
            'Configuring your firewall',
            'Starting a sync manually',
            'Synchronizing automatically',
            'Synchronizing Outlook Notes',
            'Synchronizing new data from phone to computer',
            'Synchronizing your phone with two or more computers',
            ]
        },{
        'name':'Direct me on how to do the following Trello task:',
        'tasklist':[
            'Create A Board',
            'Add Lists',
            'Invite Members',
            'Setting privacy settings',
            'Create Cards From Email',
            'Mark Cards Done',
            'Import Items Instantly',
            'Team Visibility',
            'linking your Trello and Slack teams to foster seamless collaboration between the two apps',
            'Add Another Admin (Or Three)',
            'Add new members to your team',
            'Remove someone from the team',
            'Add Members to cards to assign people to tasks',
            'Add Checklists for cards that require subtasks',
            'Add a Due date to cards with deadlines',
            'Add Attachments',
            ]
        },{
        'name':'Direct me on how to do the following Snagit task:',
        'tasklist':[
            'Panoramic Capture',
            'Scrolling Capture',
            'Save Capture Settings',
            'Capture Text',
            'Add Capture Info to Your Image',
            'Create an Animated GIF',
            'Working With Selection Tools',
            'Using the Translation Workflow',
            ]
        },{
        'name':'Direct me on how to do the following Recuva task:',
        'tasklist':[
            'Recover deleted files',
            'Recovering files from damaged or reformatted disks',
            ]
        },
]

def support_list_length():
    l = []
    for i in SUPPORT:
        for j in i.values()[0]:
            l.append(j)

    return l

            
            
            
            