.. sknrf documentation introduction file

..  figure:: ../_images/PNG/sknrf_logo.png
    :width: 500 pt
    :align: center

Jenkins
=======

.. tip::
    Each computer has an user called jenkins and a group called jenkins. All computers use the same UID and GID. (If you have access to NIS, this can be done more easily.) This is not a Jenkins requirement, but it makes the agent management easier.

.. tip::
    On each computer, /var/jenkins directory is set as the home directory of user jenkins. Again, this is not a hard requirement, but having the same directory layout makes things easier to maintain.
.. tip::
    All machines run sshd. Windows agents run cygwin sshd.
.. tip::
    All machines have /usr/sbin/ntpdate installed, and synchronize clock regularly with the same NTP server.
.. tip::
    Master's /var/jenkins have all the build tools beneath it --- a few versions of Ant, Maven, and JDKs. JDKs are native programs, so I have JDK copies for all the architectures I need. The directory structure looks like this:

    +----+----+----+------------------------------------------------------------------+
    | /var/jenkins                                                                    |
    +----+----+----+------------------------------------------------------------------+
    |    |+- .ssh                                                                     |
    +----+----+----+------------------------------------------------------------------+
    |    |+- bin                                                                      |
    +----+----+----+------------------------------------------------------------------+
    |    |    |+- agent  (more about this below)                                      |
    +----+----+----+------------------------------------------------------------------+
    |    |+- workspace (jenkins creates this file and store all data files inside)    |
    +----+----+----+------------------------------------------------------------------+
    |    |+- tools                                                                    |
    +----+----+----+------------------------------------------------------------------+
    |    |    |+- ant-1.5                                                             |
    +----+----+----+------------------------------------------------------------------+
    |    |    |+- ant-1.6                                                             |
    +----+----+----+------------------------------------------------------------------+
    |    |    |+- maven-1.0.2                                                         |
    +----+----+----+------------------------------------------------------------------+
    |    |    |+- maven-2.0                                                           |
    +----+----+----+------------------------------------------------------------------+
    |    |    |+- java-1.4 -> native/java-1.4 (symlink)                               |
    +----+----+----+------------------------------------------------------------------+
    |    |    |+- java-1.5 -> native/java-1.5 (symlink)                               |
    +----+----+----+------------------------------------------------------------------+
    |    |    |+- java-1.8 -> native/java-1.8 (symlink)                               |
    +----+----+----+------------------------------------------------------------------+
    |    |    |+- native -> solaris-sparcv9 (symlink; different on each computer)     |
    +----+----+----+------------------------------------------------------------------+
    |    |    |+- solaris-sparcv9                                                     |
    +----+----+----+------------------------------------------------------------------+
    |    |    |    |+- java-1.4                                                       |
    +----+----+----+------------------------------------------------------------------+
    |    |    |    |+- java-1.5                                                       |
    +----+----+----+------------------------------------------------------------------+
    |    |    |    |+- java-1.8                                                       |
    +----+----+----+------------------------------------------------------------------+
    |    |    |+- linux-amd64                                                         |
    +----+----+----+------------------------------------------------------------------+
    |    |    |    |+- java-1.4                                                       |
    +----+----+----+------------------------------------------------------------------+
    |    |    |    |+- java-1.5                                                       |
    +----+----+----+------------------------------------------------------------------+
    |    |    |    |+- java-1.8                                                       |
    +----+----+----+------------------------------------------------------------------+

Getting Started
---------------

Install Jenkins
~~~~~~~~~~~~~~~
    Install Jenkins

Activate Jenkins
~~~~~~~~~~~~~~~~

.. code-block:: bash

        >>>sudo cat /Users/Shared/Jenkins/Home/secrets/initialAdminPassword

Install Suggested Plugins
~~~~~~~~~~~~~~~~~~~~~~~~~
Create First Admin User
Add environment variables for master node:

.. code-block:: bash

        >>>PATH+EXTRA = /usr/local/bin

Add pipeline
~~~~~~~~~~~~

.. code-block:: groovy

    pipeline {
        agent {label 'master'}
        stages {
            stage('build') {
                steps {
                    sh 'python --version'
                }
            }
        }
    }

Create Jenkins Group/User on Remote machine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Windows
"""""""
- Windows + r: lusrmgr.msc
- Add User jenkins
- Add jenkins to Administrators group

Linux
"""""

.. code-block:: bash

    >>>sudo groupadd jenkins
    >>>sudo useradd -m -s /bin/bash jenkins
    >>>sudo passwd jenkins
    >>>sudo usermod -a -G jenkins jenkins

Enable Port Forwarding on VMs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
VirtualBox->Settings->Network->Adapter1->Advanced->Port Forwarding
Protocol: TCP Host IP: 127.0.0.1 Host Port: 2222 Guest IP: 10.0.2.15 Guest Port: 22

Enable SSH Server
~~~~~~~~~~~~~~~~~

Windows
"""""""
Using powershell as admin:

.. code-block:: bash

    >>>Get-WindowsCapability -Online | ? Name -like 'OpenSSH*'
    >>>Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0
    >>>Start-Service sshd
    >>>cd C:\ProgramData\ssh
    >>>Set-Service -Name sshd -StartupType 'Automatic'
    >>>Get-NetFirewallRule -Name *ssh*

There should be a firewall rule named "OpenSSH-Server-In-TCP", which should be enabled

SSH into Machine
~~~~~~~~~~~~~~~~

Create Private/Public Keys on Master and Slave
""""""""""""""""""""""""""""""""""""""""""""""

On the Master machine:

.. code-block:: bash

    >>>ssh-keygen -t rsa

On the Slave machine:

.. code-block:: bash

    >>>ssh-keygen -t dsa

Add Master to Authorized keys on Slave
""""""""""""""""""""""""""""""""""""""

On the Master machine:

.. code-block:: bash

    >>>cat ~/.ssh/id_dsa.pub | ssh -p 2222 login@slave 'cat > ~/.ssh/authorized_keys'

Add Slave to Known Hosts on Master
""""""""""""""""""""""""""""""""""

On the Master machine:

.. code-block:: bash

    >>>ssh -p 2222 login@slave '~/.ssh/id_dsa.pub' > ~/.ssh/known_hosts

Add Node in Jenkins
~~~~~~~~~~~~~~~~~~~

Manage Jenkins -> Manage Nodes
    * Name: linux openSUSE
    * Permanent Agent: True
    * Remote Root Directory: /home/jenkins
    * Labels: linux openSUSE
    * Usage: Only build jobs with label expressions matching this node
    * Launch Method: Launch Agents using SSH
    * Host: 127.0.0.1
    * Credentials: login/password
    * Host Key Verification Strategy




