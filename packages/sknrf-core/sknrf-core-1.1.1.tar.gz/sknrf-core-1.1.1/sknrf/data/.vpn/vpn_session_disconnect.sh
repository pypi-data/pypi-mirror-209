#!/bin/bash
/usr/bin/openvpn3 session-manage --config client.ovpn --disconnect
printf 'YES\n' | /usr/bin/openvpn3 config-remove --config client.ovpn
