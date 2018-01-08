# coding: utf8
'''
Task lists
'''
SECURITY = [
    {
        'name':'computer security',
        'tasklist':[
            'test'
        ]
    },
    {
        'name':'network security',
        'tasklist':[
            'Denial of Service',
            'Distributed Denial of Service',
            'Unauthorized Access',
            'Eavesdropping',
            'IP Spoofing',
            'Man-in-the-middle-attack',
            'Viruses and Worms',
            'Trojan Horses',
            'SPAM',
            'Phishing',
            'Packet Sniffers',
            'Maliciously Coded Websites',
            'Password Attacks',
            'Zombie Computers and Botnets'
        ]
        },
    {
        'name':'network security solutions',
        'tasklist':[
            'Enforce strong authentication strategies'
            'Entertaining encryption strategy',
            'Apply network segmentation',
            'Employing Network Access Control',
            'Filtering of packets',
            'ACLs helps prevent Spoofing',
            'SSL certificates',
            'Using Public Key Infrastructures based authentications',
            'Time testing techniques',
            'Update your patches',
            'Upgrading Firewalls with ACLs (Access Control Lists)',
            'Demilitarized Zone (DMZ)',
            'Proxy',
            'Install Anti-Virus Software',
            'Employ a firewall to protect networks',
            'Filter all email traffic',
            'Educate all users to be careful of suspicious e-mails',
            'Implement a vulnerability management program',
            'Make regular backups of critical data',
            'Develop an Information Security Policy',
            'Develop an Incident Response Plan',
            'Steal the network ',
            'Stateful Packet Inspection',
            'Network Address Translation (NAT)',
            'Closing unused ports',
            'Install IDS/IPS with the ability to track floods (such as SYN, ICMP, etc.)',
            'Install a firewall',
            'Ensure that HTTP opens session’s time out at a reasonable time',
            'Ensure that TCP also time out at a reasonable time'
        ]
        },
]

def security_list_length():
    l = []
    for i in SECURITY:
        for j in i.values()[0]:
            l.append(j)

    return l