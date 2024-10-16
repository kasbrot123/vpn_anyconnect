# vpn_anyconnect

Batch Script and Python Script for Cisco Anyconnect Auto Connect with TOTP


## Description

Basic python script to connect to a vpn server with user name, password and TOTP access token. I wrote the script to automate the login of the vpn client because it was anoying to enter password and TOTP access token.

---

## Issues

If vpn is connected and you run the python script again to connect to the vpn the process will get stuck because of the Cisco Anyconnect client, anyways for me it works. (**TODO:** Check if connected to vpn and prevent freeze. ) 


