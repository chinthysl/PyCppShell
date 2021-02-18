# PyCppShell

Combination of Python, C++, and Shell script regarding basic socket programming and web services.

- [ShellScripts](#ShellScripts)
- [CppCodes](#CppCodes)
- [ShellScripts](#PythonCodes)


## ShellScripts
- WebSearch.sh - A script that recursively downloads a given webpage and finds all hyperlink in that webpage. It should then explore all the hyperlinks and carry doing that in a recursive way. In each of this recursive crawling, it finds all the appearance of the given search word and displays them. The script takes in parameters while execution in the format: 
```
./script.sh “website_address” “search_word” 
Ex: ./script.sh www.usec.io Ninja
```
- DropIPs.sh - A script that blocks a connection from a given range of IP address for a particular duration. You are allowed to use either IPTables or/and network interfaces. The script takes a file with the list of IP addresses as input and another parameter as duration (in minutes). Example: ./DropIps.sh “ip.blocked” 60 Where file contains the IP addresses separated by newline as shown below and 60 minutes is the duration for which these IP addresses won’t be able to connect to any port on the given system. Example content of “file”: 10.21.11.14 202.14.56.22 192.168.1.2

```
cd ShellScripts
./WebSearch.sh
sudo ./DropIPs.sh ip.blocked
```

## CppCodes
- Server.cpp - A socket server program that listens on port 2999. Through this socket program you are able to execute the script in Shell Programming section above. This socket server program is a system service which can be controlled by systemctl (like start, stop and restart this socket server).
- Client.cpp - A client socket program for testing it. (In other words, by using a test client program in running on one computer, a user is able to connect to another computer socket and execute the script on it.)
- PThread.cpp - A program in C++ using the pthread library that waits for user input from the command line. The user enters a positive integer n. The process creates n threads, so there are n + 1 threads in total Each of the n threads:
prints its thread id to the standard output -
sleeps for between 1 to 10 seconds. The duration is a random positive integer.
prints "thread id ___ is exiting"
exits. The first thread prints to the standard output:
the return code and
the thread id of each of the exiting threads. The first thread then exits. You may use any part of the GNU C Library or C++11 and assume that the platform is Linux.
C++11 compiler is used for compilation
```
cd CppCodes
g++ Client.cpp -o client g++ Server.cpp -o server
./server 
./client
g++ PThreads.cpp -o pthreads -lpthread ./pthreads
```


## PythonCodes
- Server2999.py - A python socket server program that listens on port 3111 and forwards the request to port 2999 (the socket server from first problem of C++ programming question). In other words, when a client user (Client3111.py) connects to port 3111, the python socket server issues a request internally to connect to port 2999 and passes all the data/socket information to port 2999. And similarly, any data returned from the service (server from the previous problem of C++ programming) to Python socket program is returned all the way back to the client user which initially connected to port 3111. Here is how it looks:
```
C++ Socket Server on 2999 <-----> Python Socket Server on 3111 <-----> Client User 3111
```
- PacketDecoder.py - A program that displays all the data packet that flows through the given network interface. For example, if network interface eth0 is selected, it displays all the incoming and outgoing packets through this network interface. While displaying a packet, showing incoming IP address, port, destination IP address.

```
cd CppCodes 
./server
cd ../PythonCodes
python3 ServerClientInterface.py
python3 Client3111.py
python3 PacketDecoder.py
```
