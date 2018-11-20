# DFS2018


sha1sum - f78e38ed30a0473f85b96d0593800e6a39512bb1 

DFS system for Lab assignment by Damir, Atadjan and Luis.


![Screenshot](https://github.com/Dzhan85/DFS2018/blob/master/dream-team-arrow-tag-sign-260nw-582103660.jpg)

## Index
+ [Features](#features)
+ [Installation](#installation)
+ [How It Works](#how-it-works)


## Features<a name="features"></a>
A distributed file system (DFS) is a file system with data stored on a server. The data is accessed and processed as if it was stored on the local client machine. The DFS makes it convenient to share information and files among users on a network in a controlled and authorized way. The server allows the client users to share files and store data just like if they were storing the information locally.

#### Architecture

![Screenshot](https://github.com/Dzhan85/DFS2018/blob/master/DFS%20NEW.png)

## Installation<a name="installation"></a>

 DFS can be tested on the Docker container , it can be pushed from docker cloud or from github repository . To start using,    script should be run. This script starts  with name server. Storage Servers are running by   command. Client needs   command.
Docker images:
```
push for storage server
$docker push domer/dsproj-storsrv

push client
$docker push domer/dsproj-client

push nameserver
$docker push domer/dsproj-namesrv

````



### Running Locally
Make sure you have [Python](https://www.python.org/downloads/), [pyftpdlib](https://pypi.org/project/pyftpdlib/), [PyOpenSSL](https://pypi.org/project/pyOpenSSL/) and [pip](https://pypi.org/project/pip/) installed.

1. Clone or Download the repository

	```
	$ git clone https://github.com/Dzhan85/DFS2018.git
	$ cd DFS2018/
	```
2. Install Dependencies

	```
	$ pip install
	```
2. Generate PKI in folder  with your credentials(see [Setup Configurations](#configurations)).

3. Got to Storageserver folder and Run  script Storage Server(as Admin)

	```
	$ python ftpssrv.py
	
	``` 
3. Got to Nameserver folder and Run  script (as Admin)	
	```
	$ python nameserver.py
	```
	
By specifing IP addresses of storage servers.
After succesfull connection you will see IP address and port.

3. Got to Client folder and Run  script (as Admin)	
	```
	$ python client.py
	```
	
After succesfull connection you will specify IP address and port, which appeared in nameserver initialization.
	
5. Start the application

	```
	$ python ....
	```





## How It Works<a name="how-it-works"></a>


###Client
The client welcomes the user with the command line with the answer: “Type command”, this command line interface is very similar to native Linux Command Line but has some differences, for example this command interface will recognize only the commands defined in the application, to get a list of supported commands simply needs to type  ‘gethelp’ in the command line and user will see the supported command list like in the Table 1:



| Functionality |  Command | Description |
| :---: | :----------: |:--------: |
| Help |   `gethelp`   | List of commands |
| Space |   `frspace` | know avalaible space |
| List |   `fllist` | To list folder contains |
| File delete|   `makedir`| To make new directory  |
| Directory  |   `chngdir` | Switch directory|
| Read file |   `readfile ` | To read/download file |
| Write file |  `writefile`  |  To write/upload file  |
| Delete file |   `filedel ` | To delete file  |
| Size |   `filesize`    | To know size of file  |
| Remove |`remdir`| To remove folder  |
|Exit from DFS | `ftpsquit` | To close client and DFS|


### Setup Configurations<a name="configurations"></a>







### Database<a name="database"></a>




## Configuration and run in Docker

Local host preparations.

Storage service use it use default FTP 21 port for file transfer and rsync over SSH for  synchronization, hosts SSH port 22, and FTP port 21 should be changed if they used.


Run image /bin/sh with command:

```
	#docker run -it --rm --net=host domer/dsproj-storsrv /bin/sh
	```
install dependencies
```
    #apt update
    
    ```
during ssh installation you will be asked about config file, choose second variant:
   ``` #apt install  ssh```
   
   
   
   
   ```
    #apt install rsync
```

Start ssh service:
```
    # service ssh start
    [ ok ] Starting OpenBSD Secure Shell server: sshd.
```

Start server:

````
Server has next arguments
--secsrv, default="127.0.0.1" – server for synchronization
--homedir, default="/ftpsrv/share/" – FTP home directory
--user, default="user" – FTP user name
--passwd, default="12345" – FTP user password
```

Run server with:
```
    #python ftpssrv.py --secsrv <IPv4 of second srver>
 ```  




