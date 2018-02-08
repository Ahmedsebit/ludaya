# coding: utf8
'''
Task lists
'''
SERVER = [
    {
        'name':'Active Directory real time issues and solutions',
        'tasklist':[
            'DNS Entry of Domain Controller is Resolving to Incorrect value',
            'Replsummary showing unknown for largest delta on AD replication checks',
            'Domain Controller failed test Machineaccount on DCDIAG',
            'AD Slow Authentication and prompting for credentials again and again',
            'How secure channel determine the Domain controller in cross-forest',
            'Active directory Troubleshooting',
            'Active Directory Replication failed with ...Target principal name is incorrect',
            "Replication failed with ...The destination server is currently rejecting replication requests.. Error",
            'Troubleshoot Active Directory Server Replication'
        ]
    },
    {
        'name':'Group Policy (GPO) real time issues and solutions',
        'tasklist':[
            'Issue managing IE configuration through GPO',
            'Why we cant edit/view windows 2008 Vista and windows 7 GPO settings from windows 2003',
            'Gpresult failed with ERROR Access Denied',
            'Home page URL not working for IE7',
            'GPO update failed in Slow Link VPN site with Event ID 1000 and 1054',
            'Group Policy Processing over Slow Links',
            'Group Policy slow link detection on windows server 2008'
        ]
    },
    {
        'name':'Real time issues and solutions',
        'tasklist':[
            'Account lockout',
            'How to resolve the Print Spooler service crash issue (Print spooler service is not running)',
            'How to find the domain controller that contains the lingering object',
            'Reconfigure roaming profile folder and home folder permission for all the users',
            'Roaming profile issues'
        ]
    },
    {
        'name':'Active Directory Questions',
        'tasklist':[
            'I have a single Active Directory domain. All domain controllers run Windows Server 2008 and are configured as DNS servers. The domain contains one Active Directory-integrated DNS zone. I need to ensure that outdated DNS records are automatically removed from the DNS zone. What should I do?',
            'My network consists of a single Active Directory domain. All domain controllers run Windows Server 2008 R2. The Audit account management policy setting and Audit directory services access setting are enabled for the entire domain. I need to ensure that changes made to Active Directory objects can be logged. The logged changes must include the old and new values of any attributes. What should I do?',
            'My company, Contoso, Ltd., has a main office and a branch office. The offices are connected by a WAN link. Contoso has an Active Directory forest that contains a single domain named ad.contoso.com. The ad.contoso.com domain contains one domain controller named DC1 that is located in the main office. DC1 is configured as a DNS server for the ad.contoso.com DNS zone. This zone is configured as a standard primary zone. I install a new domain controller named DC2 in the branch office. I install DNS on DC2. I need to ensure that the DNS service can update records and resolve DNS queries in the event that a WAN link fails. What should I do?',
            'The ad.contoso.com domain contains one domain controller named DC1 that is located in the main office. DC1 is configured as a DNS server for the ad.contoso.com DNS zone. This zone is configured as a standard primary zone. I install a new domain controller named DC2 in the branch office. I install DNS on DC2. I need to ensure that the DNS service can update records and resolve DNS queries in the event that a WAN link fails. What should I do?',
            'My company has a server that runs an instance of Active Directory Lightweight Directory Service (AD LDS). I need to create new organizational units in the AD LDS application directory partition. What should I do?',
            'My company has an Active Directory domain. The company has twodomain controllers named DC1 and DC2. DC1 holds the Schema Master role. DC1 fails. I log on to Active Directory by using the administrator account. I are not able to transfer the Schema Master operations role. I need to ensure that DC2 holds the Schema Master role. What should I do?',
            'My company has an Active Directory forest that runs at the functional level of Windows Server 2008. I implement Active Directory Rights Management Services (AD RMS). I install Microsoft SQL Server 2005. When I attempt to open the AD RMS administration Web site, I receive the following error message: "SQL Server does not exist or access denied." I need to open the AD RMS administration Web site. Which two actions should I perform?',
            'My network consists of an Active Directory forest that contains one domain named contoso.com. All domain controllers run Windows Server 2008 R2 and are configured as DNS servers.  I have two Active Directory-integrated zones: contoso.com and nwtraders.com. I need to ensure a user is able to modify records in the contoso.com zone. I must prevent the user from modifying the SOA record in the nwtraders.com zone. What should I do?',
            'My company has an Active Directory domain. All servers run Windows Server 2008 R2. My company uses an Enterprise Root certificate authority (CA). I need to ensure that revoked certificate information is highly available. What should I do?',
            'I have two servers named Server1 and Server2. Both servers run Windows Server 2008 R2. Server1 is configured as an enterprise root certification authority (CA). I install the Online Responder role service on Server2. I need to configure Server1 to support the Online Responder. What should I do?',
            'My company has an Active Directory domain. A user attempts to log on to a computer that was turned off for twelve weeks. The administrator receives an error message that authentication has failed. I need to ensure that the user is able to log on to the computer. What should I do?',
            'My company has an Active Directory forest that contains a single domain. The domain member server has an Active Directory Federation Services (AD FS) role installed. I need to configure AD FS to ensure that AD FS tokens contain information from the Active Directory domain. What should I do?',
            'I network consists of a single Active Directory domain. All domain controllers run Windows Server 2008 R2. I need to reset the Directory Services Restore Mode (DSRM) password on a domain controller. What tool should I use?',
            'My company has a main office and a branch office. I deploy a read-only domain controller (RODC) that runs Microsoft Windows Server 2008 to the branch office. I need to ensure that users at the branch office are able to log on to the domain by using the RODC. What should I do?',
            'My company has a single Active Directory domain named intranet.adatum.com. The domain controllers run Windows Server 2008 and the DNS server role. All computers, including non-domain members, dynamically register their DNS records. I need to configure the intranet.adatum.com zone to allow only domain members to dynamically register DNS records. What should I do?',
            'My network consists of a single Active Directory domain. All domain controllers run Windows Server 2008 R2 and are configured as DNS servers. A domain controller named DC1 has a standard primary zone for contoso.com. A domain controller named DC2 has a standard secondary zone for contoso.com. I need to ensure that the replication of the contoso.com zone is encrypted. I must not lose any zone data. What should I do?',
            'I are decommissioning domain controllers that hold all forest-wide operations master roles. I need to transfer all forest-wide operations master roles to another domain controller. Which two roles should I transfer?',
            'Contoso, Ltd. has an Active Directory domain named ad.contoso.com. Fabrikam, Inc. has an Active Directory domain named intranet.fabrikam.com. Fabrikams security policy prohibits the transfer of internal DNS zone data outside the Fabrikam network. I need to ensure that the Contoso users are able to resolve names from the intranet.fabrikam.com domain. What should I do?',
            'An Active Directory database is installed on the C volume of a domain controller. I need to move the Active Directory database to a new volume. What should I do?',
            'My company has file servers located in an organizational unit named Payroll. The file servers contain payroll files located in a folder named Payroll. I create a GPO. I need to track which employees access the Payroll files on the file servers. What should I do?',
            'My company uses a Windows 2008 Enterprise certificate authority (CA) to issue certificates. I need to implement key archival. What should I do?',
            'My company has an Active Directory domain that runs Windows Server 2008 R2. The Sales OU contains an OU for Computers, an OU for Groups, and an OU for Users. I perform nightly backups. An administrator deletes the Groups OU. I need to restore the Groups OU without affecting users and computers in the Sales OU. What should I do?',
            'My network consists of a single Active Directory domain. The functional level of the forest is Windows Server 2008 R2. I need to create multiple password policies for users in My domain. What should I do?',
            'I have a domain controller that runs Windows Server 2008 R2 and is configured as a DNS server. I need to record all inbound DNS queries to the server. What should I configure in the DNS Manager console?',
            'My company has a main office and a branch office. The company has a single-domain Active Directory forest. The main office has two domain controllers named DC1 and DC2 that run Windows Server 2008 R2. The branch office has a Windows Server 2008 R2 read-only domain controller (RODC) named DC3. All domain controllers hold the DNS Server role and are configured as Active Directory-integrated zones. The DNS zones only allow secure updates. I need to enable dynamic DNS updates on DC3. What should I do?',
            'My company has an Active Directory domain named ad.contoso.com. The domain has two domain controllers named DC1 and DC2. Both domain controllers have the DNS server role installed. I install a new DNS server named DNS1.contoso.com on the perimeter network. I configure DC1 to forward all unresolved name requests to DNS1.contoso.com. I discover that the DNS forwarding option is unavailable on DC2. I need to configure DNS forwarding on the DC2 server to point to the DNS1.contoso.com server. Which two actions should I perform? (Each correct answer presents part of the solution. Choose two.)',
            'My company has an organizational unit named Production. The Production organizational unit has a child organizational unit named R&D. I create a GPO named Software Deployment and link it to the Production organizational unit. I create a shadow group for the R&D organizational unit. I need to deploy an application to users in the Production organizational unit. I also need to ensure that the application is not deployed to users in the R&D organizational unit. What are two possible ways to achieve this goal? (Each correct answer presents a complete solution. Choose two.)',
            'My company has a branch office that is configured as a separate Active Directory site and has an Active Directory domain controller. The Active Directory site requires a local Global Catalog server to support a new application. I need to configure the domain controller as a Global Catalog server. Which tool should I use?',
            'My company has a main office and three branch offices. The company has an Active Directory forest that has a single domain. Each office has one domain controller. Each office is configured as an Active Directory site. All sites are connected with the DEFAULTIPSITELINK object. I need to decrease the replication latency between the domain controllers. What should I do?',
            'My company has two Active Directory forests named contoso.com and fabrikam.com. Both forests run only domain controllers that run Windows Server 2008. The domain functional level of contoso.com is Windows Server 2008. The domain functional level of fabrikam.com is Windows Server 2003 Native mode. I configure an external trust between contoso.com and fabrikam.com. I need to enable the Kerberos AES encryption option. What should I do?',
            'All consultants belong to a global group named TempWorkers. I place three file servers in a new organizational unit named SecureServers. The three file servers contain confidential data located in shared folders. I need to record any failed attempts made by the consultants to access the confidential data. Which two actions should I perform? (Each correct answer presents part of the solution. Choose two.)',
            'I have two servers named Server1 and Server2. Both servers run Windows Server 2008 R2. Server1 is configured as an Enterprise Root certification authority (CA). I install the Online Responder role service on Server2. I need to configure Server2 to issue certificate revocation lists (CRLs) for the enterprise root CA. Which two tasks should I perform? (Each correct answer presents part of the solution. Choose two.)',
            'My company has an Active Directory forest. The forest includes organizational units corresponding to the following four locations: London ,Chicago, New York, India Each location has a child organizational unit named Sales. The Sales organizational unit contains all the users and computers from the sales department. The offices in London, Chicago, and New York are connected by T1 connections. The office in India is connected by a 256-Kbps ISDN connection. I need to install an application on all the computers in the sales department. Which two actions should I perform? (Each correct answer presents part of the solution. Choose two.)',
            'My company has a domain controller server that runs the Windows Server 2008 R2 operating system. The server is a backup server. The server has a single 500-GB hard disk that has three partitions for the operating system, applications, and data. I perform daily backups of the server. The hard disk fails. I replace the hard disk with a new hard disk of the same capacity. I restart the computer on the installation media. I select the Repair My computer option. I need to restore the operating system and all files. What should I do?',
            'I need to remove the Active Directory Domain Services role from a domain controller named DC1. What should I do?',
            'My company has an Active Directory forest. The company has branch offices in three locations. Each location has an organizational unit. I need to ensure that the branch office administrators are able to create and apply GPOs only to their respective organizational units. Which two actions should I perform? (Each correct answer presents part of the solution. Choose two.)',
            'My company has an Active Directory domain. A user attempts to log on to the domain from a client computer and receives the following message: "This user account has expired. Ask My administrator to reactivate the account." I need to ensure that the user is able to log on to the domain. What should I do?',
            'I have an existing Active Directory site named Site1. I create a new Active Directory site and name it Site2. I need to configure Active Directory replication between Site1 and Site2. I install a new domain controller. I create the site link between Site1 and Site2.',
            'My company has an Active Directory forest. Each branch office has an organizational unit and a child organizational unit named Sales. The Sales organizational unit contains all users and computers of the sales department. I need to install an Office 2007 application only on the computers in the Sales organizational unit. I create a GPO named SalesApp GPO. What should I do next?',
            'My network consists of an Active Directory forest that contains one domain. All domain controllers run Windows Server 2008 R2 and are configured as DNS servers. I have an Active Directory- integrated zone. I have two Active Directory sites. Each site contains five domain controllers. I add a new NS record to the zone. I need to ensure that all domain controllers immediately receive the new NS record. What should I do?',
            'My company has a single Active Directory domain named intranet.contoso.com. All domain controllers run Windows Server 2008 R2. The domain functional level is Windows 2000 native and the forest functional level is Windows 2000. I need to ensure the UPN suffix for contoso.com is available for user accounts. What should I do first?',
            'I have a Windows Server 2008 R2 Enterprise Root CA . Security policyprevents port 443 and port 80 from being opened on domain controllers and on the issuing CA . I need to allow users to request certificates from a Web interface. I install the Active Directory Certificate Services (AD CS) server role. What should I do next?',
        ]
    }
]

def server_list_length():
    l = []
    for i in SERVER:
        for j in i.values()[0]:
            l.append(j)

    return l
