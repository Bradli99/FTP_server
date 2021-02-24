import os, sys
import socket

print(f'Visit "ftp://{socket.gethostbyname(socket.gethostname())}" in your browser so you can access, choose & download files.')
print('Note: Don\'t close this, otherwise the FTP server will be closed too during transfer.')

if sys.platform == 'linux' and 'win' not in sys.platform:
	os.system('python3 -m pyftpdlib -p 21 w') # In case of Linux
elif 'win' in sys.platform and 'linux' not in sys.platform:
	os.system('python -m pyftpdlib -p 21 w') # In case of Windows