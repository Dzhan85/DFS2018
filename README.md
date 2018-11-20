# DFS2018


sha1sum - f78e38ed30a0473f85b96d0593800e6a39512bb1 

DFS system for Lab assignment by


![Screenshot](https://github.com/Dzhan85/DFS2018/blob/master/dream-team-arrow-tag-sign-260nw-582103660.jpg)

## Index
+ [Features](#features)
+ [Installation](#installation)
+ [How It Works](#how-it-works)


## Features<a name="features"></a>
A distributed file system (DFS) is a file system with data stored on a server. The data is accessed and processed as if it was stored on the local client machine. The DFS makes it convenient to share information and files among users on a network in a controlled and authorized way. The server allows the client users to share files and store data just like if they were storing the information locally.



## Installation<a name="installation"></a>

 DFS can be tested on the Docker container , it can be pushed from docker cloud or from github repository . To start using,    script should be run. This script starts  with name server. Storage Servers are running by   command. Client needs   command.
Docker images:
```
$docker push domer/dsproj-storsrv
$docker push domer/dsproj-client
$docker push domer/dsproj-namesrv
````



### Running Locally
Make sure you have [Python](https://www.python.org/downloads/),  and [pip](https://pypi.org/project/pip/) installed.

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

3. Run Storage Server(as Admin)

	```
	$ python 
	``` 
5. Start the application

	```
	$ python ....
	```





## How It Works<a name="how-it-works"></a>


###Client

The client welcomes the user with the command line. This command line interface is very similar to native Linux Command Line but has some differences. A supported command are shown in the Table 1:



| Functionality |  Command | Description |
| :---: | :----------: |:--------: |
| Initialize |   `init`   | Initialize system, search a new Name Server in the local network |
| File Read  |   `rd /path/filename` | This command downloads file to cache |
| File write |   `wr filename` | Upload file to Storage Service from the cache. |
| File delete|   `rm /path/filename`| Removing the file from the DFS  |
| File info  |   `info /path/filename` | Shows date of creating, size of the file and adress of the Storage Server|
| Open directory |   `cd /pathToFolder   ` or `cd folder ` | Changes current directory. Can be direct and relative path to the folder. Maintains `.` and `..` signs |
| Read directory |  `ls /path` or `ls`  |  List files and directory  inside the directory  |
| Make directory |   `mkdir folderName` | Makes a directory in the current    directory  |
| Delete directory|   `rm folderName`    | Deletes folder if the folder does not exist files.  |
| Linux Command Line Commands |`nano file`, `more file`, `cat file`, `tail file`| Executes utilities on the file from DFS. Some utilities and commands can be crashed or not working in this mode.  |
|Exit from DFS | `ex` or `exit` | Exites from the DFS|


### Setup Configurations<a name="configurations"></a>







### Database<a name="database"></a>


#### Schemas

###




