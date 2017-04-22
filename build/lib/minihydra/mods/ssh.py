import paramiko
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('192.168.8.248', 22, username='root', password='password', timeout=4)
stdin, stdout, stderr = client.exec_command('ls -l')
for std in stdout.readlines():
    print std,
client.close()