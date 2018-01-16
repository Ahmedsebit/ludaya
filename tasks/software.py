# coding: utf8
'''
SOFTWARE Task lists
'''
SOFTWARE = [
    {
        'name':'Kindly prepare evaluations for this software which we are planning to use',
        'tasklist':[
            'Wave for Accounting and Invoicing ',
            'SCORE a Business templates and tools',
            'CRM-Zoho CRM',
            'Draw.io for Diagramming',
            'MailChimp for Email marketing',
            'Dropbox for File backup and management',
            'Recuva for File recovery',
            'Skype for Online meetings',
            'AkrutoSync for Outlook sync',
            'PicMonkey for Photo editor',
            'Trello for Project management',
            'TinyScan for Scanner',
            'Snagit for Screen capture',
            'Chrometa for Time tracking',
            'Buffer and Hootsuite for Social media management',
        ]
        },
    {
        'name':'Kindly prepare evaluations for this hardware hardware',
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
        'name':'Kindly establish requirements for a new system  which we are planning to acquire for:',
        'tasklist':[
            'Accounting and Invoicing',
            'Business templates and tools',
            'CRM-Zoho CRM',
            'Diagramming',
            'Email marketing',
            'File backup and management',
            'File recovery',
            'Online meetings',
            'Outlook sync',
            'Photo editor',
            'Project management',
            'Scanner',
            'Screen capture',
            'Time tracking',
            'Social media management',
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

    {
        'name':'Configure software',
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

def software_list_length():
    l = []
    for i in SOFTWARE:
        for j in i.values()[0]:
            l.append(j)

    return l