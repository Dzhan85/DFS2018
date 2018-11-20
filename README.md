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
Make sure you have [Node.js](https://nodejs.org/) and [npm](https://www.npmjs.com/) installed.

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
3. Download and Install [Redis](http://redis.io/download).
4. Running Redis Server(as Admin)

	```
	$ 
	``` 
5. Start the application

	```
	$ npm start
	```





## How It Works<a name="how-it-works"></a>



### Setup Configurations<a name="configurations"></a>







### Database<a name="database"></a>


#### Schemas

###




