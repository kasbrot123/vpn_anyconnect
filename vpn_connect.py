import pyotp
import subprocess
from credentials import *


VPNCLI = r'C:\Program Files (x86)\Cisco\Cisco Secure Client\vpncli.exe'


totp = pyotp.TOTP(TOTP_TOKEN, digits=6, interval=60, digest='SHA256')
totp_digits = totp.now()

credentials = [
        'connect {}'.format(VPNADDRESS),
        USERNAME,
        PASSWORD,
        totp_digits
        ]

STDIN = '\n'.join(credentials)



# old solution
# I create a temporary file with the credentials

# f = open('credentials.txt', 'w')
# f.write(STDIN)
# f.close()
# os.system(VPNCLI + ' -s < credentials.txt')
# os.remove('credentials.txt')


"""
vpncli.exe -s < credentials.txt

----------------
credentials.txt:
----------------
connect <vpn.domain.com>
<username>
<password>
<otp_password>
y


"""


command = [VPNCLI, "-s"]
process = subprocess.Popen(command,
                           stdin=subprocess.PIPE,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE,
                           universal_newlines=True)


stdout, stderr = process.communicate(input="connect {}\n{}\n{}\n{}\ny\n".format(VPNADDRESS, USERNAME, PASSWORD, totp_digits))
print('connected to VPN')

# print(stdout)

# if stderr:
#     print("Error:", stderr)
# else:
#     print("VPN connected successfully.")


# print('kill process')
# process.kill()

