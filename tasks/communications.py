# coding: utf8
'''
COMMUNICATION Task lists
'''
COMMUNICATION = [
    {
        'name':'Prepare evaluations of software',
        'tasklist':[
            'Accounting and Invoicing-Wave',
            'Business templates and tools-SCORE',
            'CRM-Zoho CRM',
            'Diagramming-Draw.io',
            'Email marketing-MailChimp',
            'File backup and management-Dropbox',
            'File recovery-Recuva',
            'Online meetings-Skype',
            'Outlook sync-AkrutoSync',
            'Photo editor-PicMonkey',
            'Project management-Trello',
            'Scanner-TinyScan',
            'Screen capture-Snagit',
            'Time tracking-Chrometa',
            'Social media management-Buffer and Hootsuite',
        ]
        },
    {
        'name':'Prepare evaluations of hardware',
        'tasklist':[
            'Accounting and Invoicing-Wave',
            'Business templates and tools-SCORE',
            'CRM-Zoho CRM',
            'Diagramming-Draw.io',
            'Email marketing-MailChimp',
            'File backup and management-Dropbox',
            'File recovery-Recuva',
            'Online meetings-Skype',
            'Outlook sync-AkrutoSync',
            'Photo editor-PicMonkey',
            'Project management-Trello',
            'Scanner-TinyScan',
            'Screen capture-Snagit',
            'Time tracking-Chrometa',
            'Social media management-Buffer and Hootsuite',
        ]
        },
    {
        'name':'Recommend improvements or upgrades',
        'tasklist':[
            'Accounting and Invoicing-Wave',
            'Business templates and tools-SCORE',
            'CRM-Zoho CRM',
            'Diagramming-Draw.io',
            'Email marketing-MailChimp',
            'File backup and management-Dropbox',
            'File recovery-Recuva',
            'Online meetings-Skype',
            'Outlook sync-AkrutoSync',
            'Photo editor-PicMonkey',
            'Project management-Trello',
            'Scanner-TinyScan',
            'Screen capture-Snagit',
            'Time tracking-Chrometa',
            'Social media management-Buffer and Hootsuite',
        ]
        },
    {
        'name':'Establish requirements for new systems',
        'tasklist':[
            'Accounting and Invoicing-Wave',
            'Business templates and tools-SCORE',
            'CRM-Zoho CRM',
            'Diagramming-Draw.io',
            'Email marketing-MailChimp',
            'File backup and management-Dropbox',
            'File recovery-Recuva',
            'Online meetings-Skype',
            'Outlook sync-AkrutoSync',
            'Photo editor-PicMonkey',
            'Project management-Trello',
            'Scanner-TinyScan',
            'Screen capture-Snagit',
            'Time tracking-Chrometa',
            'Social media management-Buffer and Hootsuite',
        ]
        },
    {
        'name':'Establish requirements modifications',
        'tasklist':[
            'Accounting and Invoicing-Wave',
            'Business templates and tools-SCORE',
            'CRM-Zoho CRM',
            'Diagramming-Draw.io',
            'Email marketing-MailChimp',
            'File backup and management-Dropbox',
            'File recovery-Recuva',
            'Online meetings-Skype',
            'Outlook sync-AkrutoSync',
            'Photo editor-PicMonkey',
            'Project management-Trello',
            'Scanner-TinyScan',
            'Screen capture-Snagit',
            'Time tracking-Chrometa',
            'Social media management-Buffer and Hootsuite',
        ]
        },
    {
        'name':'Train end users on usage of computer software',
        'tasklist':[
            'Accounting and Invoicing-Wave',
            'Business templates and tools-SCORE',
            'CRM-Zoho CRM',
            'Diagramming-Draw.io',
            'Email marketing-MailChimp',
            'File backup and management-Dropbox',
            'File recovery-Recuva',
            'Online meetings-Skype',
            'Outlook sync-AkrutoSync',
            'Photo editor-PicMonkey',
            'Project management-Trello',
            'Scanner-TinyScan',
            'Screen capture-Snagit',
            'Time tracking-Chrometa',
            'Social media management-Buffer and Hootsuite',
        ]
        },
]

def communcation_list_length():
    l = []
    for i in COMMUNICATION:
        for j in i.values()[0]:
            l.append(j)

    return l