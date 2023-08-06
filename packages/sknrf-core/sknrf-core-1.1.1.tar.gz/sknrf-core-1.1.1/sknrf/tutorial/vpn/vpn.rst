VPN
===

Objective
---------

Connect to the Fabrinet VPN and remote into a TILE test computer

Requirements
------------

The following files are needed:

Procedure
---------

2. Download VPN Client
~~~~~~~~~~~~~~~~~~~~~~

The following procedure is used to install the **VPN Client** and **client.ovpn** config file.

    #. Open Chromium:
        - Navigate to the enter the **VPN Server Public IP Address: 54.176.113.147**
    #. Your connection is not private
        - Press **Advanced**
        - Press **Proceed to ... (unsafe)**
    #. User Login
        - Enter username: **tilemasters** for a dynamic ip-address or **tile<#>** for a static ip-address.
        - Enter password: ``************``
    #. Download the **OpenVPN3 Client**
        - Click on the icon for your operating system.
    #. Download **Auto-Connected Profile**
        - Press **Done**

.. raw:: html

    <div class="container mt-3">
        <div id="VPNCarousel" class="carousel slide" data-ride="carousel" data-interval="false">

            <!-- Indicators -->
            <ul class="carousel-indicators">
                <li data-target="#VPNCarousel" data-slide-to="0" class="active"></li>
                <li data-target="#VPNCarousel" data-slide-to="1"></li>
                <li data-target="#VPNCarousel" data-slide-to="2"></li>
                <li data-target="#VPNCarousel" data-slide-to="3"></li>
            </ul>

            <!-- The slideshow -->
            <div class="carousel-inner">
                <div class="carousel-item active"><img src="../../_images/tutorials/vpn/PNG/img1.png" width="100%"></div>
                <div class="carousel-item"><img src="../../_images/tutorials/vpn/PNG/img2.png" width="100%"></div>
                <div class="carousel-item"><img src="../../_images/tutorials/vpn/PNG/img3.png" width="100%"></div>
                <div class="carousel-item"><img src="../../_images/tutorials/vpn/PNG/img4.png" width="100%"></div>
            </div>

            <!-- Left and right controls -->
            <a class="carousel-control-prev" href="#VPNCarousel" data-slide="prev">
            <span class="carousel-control-prev-icon"></span>
            </a>
            <a class="carousel-control-next" href="#VPNCarousel" data-slide="next">
            <span class="carousel-control-next-icon"></span>
            </a>
        </div>
    </div>

Copy the client config file to the .vpn directory:

.. code-block:: bash

    cd ${HOME}/Downloads/client.ovpn ${PCB_TESTER_DIR}/pcbtest/data/.vpn/client.ovpn

.. note:: You should now be able to connect the VPN as tilemasters using the following commands. The rest of this
   tutorial describes the advanced configuration that is deployed on each TILE system.

    .. code-block:: bash

        eval $ENV
        sudo systemctl start vpn.service                                            # Connect to VPN
        openvpn3 sessions-list                                                      # Verify VPN Connection
        sudo systemctl stop vpn.service                                             # Disconnect to VPN

3. Connect to VPN Manually
~~~~~~~~~~~~~~~~~~~~~~~~~~

Connect to the VPN manually using the following commands:

.. code-block:: bash

    openvpn3 session-start --config ${PCB_TESTER_DIR}/pcbtest/data/.vpn/client.ovpn               # Connect to VPN
    openvpn3 sessions-list                                                                        # Verify VPN Connection
    openvpn3 session-manage --config ${PCB_TESTER_DIR}/pcbtest/data/.vpn/client.ovpn --disconnect # Disconnect to VPN

4. Connect to VPN Without Credentials
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Modify the credentials in ``${PCB_TESTER_DIR}/pcbtest/data/.vpn/client.autoload``.
Then register your credentials as follows:

.. code-block:: bash

    # Perform the following in a new terminal without running eval $ENV
    openvpn3-autoload --directory ${PCB_TESTER_DIR}/pcbtest/data/.vpn/client.autoload

    openvpn3 session-start --config ${PCB_TESTER_DIR}/pcbtest/data/.vpn/client.ovpn               # Connect to VPN
    openvpn3 sessions-list                                                                        # Verify VPN Connection
    openvpn3 session-manage --config ${PCB_TESTER_DIR}/pcbtest/data/.vpn/client.ovpn --disconnect # Disconnect to VPN

5. Run the VPN Client as a Service
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Start the VPN connection at startup by running the VPN Client as a service:

.. code-block:: bash

    sudo cp -p ${PCB_TESTER_DIR}/pcbtest/data/.vpn/vpn.service /etc/systemd/system/vpn.service
    sudo cp -rfp ${PCB_TESTER_DIR}/pcbtest/data/.vpn ${HOME}/.vpn
    # sudo sed -i 's/tilemasters/tile0/g' ${HOME}/.vpn/client.ovpn                                # For static-ip address
    # sudo sed -i 's/tilemasters/tile0/g' ${HOME}/.vpn/client.autoload                            # For static-ip address
    sudo systemctl daemon-reload
    sudo systemctl enable vpn.service

    sudo systemctl start vpn.service                                                              # Connect to VPN
    systemctl status vpn.service                                                                  # Verify Service Status
    openvpn3 sessions-list                                                                        # Verify VPN Connection
    sudo systemctl stop vpn.service                                                               # Disconnect to VPN

References
----------

https://askubuntu.com/questions/1336194/how-to-connect-openvpn-automatically-on-boot-using-openvpn3-autoload
https://openvpn.net/blog/openvpn-3-linux-and-auth-user-pass/

