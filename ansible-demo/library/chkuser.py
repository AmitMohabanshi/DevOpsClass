Devops-June
Devops
Stream
Classwork
People
Devops-June
Devops
Upcoming
Woohoo, no work due soon!
View all

Share something with your class…

Announcement: "Ansible Module using Python"
mahesh kharwadkar
Created 4:32 PM4:32 PM
Ansible Module using Python

chkuser.yaml
Binary File

chkuser.py
Text

Post by gaurav mishra
gaurav mishra
Created 4:22 PM4:22 PM
14 July Recording

zoom_0.mp4
Video

Announcement: "Ansible-Custom-Module"
mahesh kharwadkar
Created 4:21 PM4:21 PM
Ansible-Custom-Module

chkprocess.sh
Text

chkprocess.yaml
Binary File

Announcement: "MANAGING HADOOP CLUSTERS WITH ANSIBLE…"
mahesh kharwadkar
Created 3:44 PM3:44 PM
MANAGING HADOOP CLUSTERS WITH ANSIBLE AND APACHE AMBARI
https://www.ansible.com/managing-hadoop-clusters-stackspace

Announcement: "Ansible E2E Project Git Hub Repo:…"
mahesh kharwadkar
Created 3:40 PM3:40 PM (Edited 3:42 PM)
Ansible E2E Project
Git Hub Repo: https://github.com/maheshkharwadkar/devops.git
Actual Path: https://github.com/maheshkharwadkar/devops/tree/master/ansible/e2eproject

Ansible-End-To-End-Project.docx
Word

Announcement: "Ansible Practice"
mahesh kharwadkar
Created Jun 30Jun 30
Ansible Practice

Ansible-Assignmnet-Prac.zip
Compressed Archive

Announcement: "Ansible Document"
mahesh kharwadkar
Created Jun 22Jun 22
Ansible Document

Ansible.pptx
PowerPoint

Ansible.docx
Word

Announcement: "Remote Install Scripts"
mahesh kharwadkar
Created Jun 16Jun 16
Remote Install Scripts

install-apache-on.sh
Text

Announcement: "Shell-Script-Docs and Sample Scripts"
mahesh kharwadkar
Created Jun 9Jun 9
Shell-Script-Docs and Sample Scripts

Exercise-08-Remote-Software-Install-02.pdf
PDF

Demo-Script.txt
Text

shellscripting.zip
Compressed Archive

Announcement: "8-Jun Recordinng"
mahesh kharwadkar
Created Jun 9Jun 9
8-Jun Recordinng

Jun-08-19.zip
Compressed Archive

#!/bin/python

DOCUMENTATION = """
---
module: chkuser
version_added: 0.1
short_description: Check if user exists on the target machine
options:
    username:
        decription:
            - Accept username from the user
        required: True
"""

EXAMPLES = """
#Usage Example
    - name: Check if user exists
      action: chkuser username=rdas
"""

def is_user_exists(username):
    try:
        import pwd
        return(username in [entry.pw_name for entry in pwd.getpwall()])
    except:
        module.fail_json(msg='Module pwd does not exists')
        

def main():
    module = AnsibleModule(
        argument_spec = dict(
            username = dict(required=True)
        )
    )   
    username = module.params.get('username')
    exists = is_user_exists(username)
    if exists:
        status = '%s user exists' % username
    else:
        status = '%s user does not exist' % username
    module.exit_json(changed=True, msg=str(status))

from ansible.module_utils.basic import *
main()
chkuser.py
Displaying chkuser.py.
