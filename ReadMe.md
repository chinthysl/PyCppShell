*************************************************************************************
***********************Instructions to compile and run*******************************
*************************************************************************************


***************Shell Programming**********

1.  Create a script that recursively downloads a given webpage and finds all hyperlink in that
    webpage. It should then explore all the hyperlinks and carry doing that in a recursive way. In
    each of this recursive crawling, it finds all the appearance of the given search word and
    displays them.
    Create the script that takes in parameters while execution in the format:
    Format: ./script.sh “website_address” “search_word”
    Example: ./script.sh www.usec.io Ninja
2.  Create a script that blocks a connection from a given range of IP address for a particular
    duration. You are allowed to use either IPTables or/and network interfaces.
    Create the script that takes a file with the list of IP addresses as input and another
    parameter as duration (in minutes).
    Example: ./script.sh “file” 60
    Where file contains the IP addresses separated by newline as shown below and 60 minutes
    is the duration for which these IP addresses won’t be able to connect to any port on the
    given system.
    Example content of “file”:
    10.21.11.14
    202.14.56.22
    192.168.1.2

cd ShellScripts

1) ./WebSearch.sh <website> <search word>
    
2) sudo ./DropIPs.sh ip.blocked <minutes>


*************C++ Programming**************

1.  Write a socket server program that listens on port 2999. Through this socket program you
    are able to execute the script that you wrote in Problem 1 of Shell Programming Question
    above. Make this socket server program a system service which can be controlled by
    systemctl (like start, stop and restart this socket server). Also write a client socket program
    for testing it. (In other words, by using a test client program in running on one computer, a
    user is able to connect to another computer socket and execute the script on it.)
2.  Write a program in C++ using the pthread library that waits for user input from the
    command line. The user enters a positive integer n. The process creates n threads, so there
    are n + 1 threads in total
    Each of the n threads:
    - prints its thread id to the standard output -
    - sleeps for between 1 to 10 seconds. The duration is a random positive integer.
    - prints "thread id ___ is exiting"
    - exits.
    The first thread prints to the standard output:
    - the return code and
    - the thread id of each of the exiting threads.
    The first thread then exits.
    You may use any part of the GNU C Library or C++11 and assume that the platform is Linux.

C++11 compiler is used for compilation

cd CppCodes
    
1) g++ Client.cpp -o client
   g++ Server.cpp -o server
    
   ./server
   ./client
    
2) g++ PThreads.cpp -o pthreads -lpthread
   ./pthreads

************Python Programming************

1.  Write a python socket server program that listens on port 3111 and forwards the request to
    port 2999 (the socket server from first problem of C++ programming question). In other
    words, when a client user connects to port 3111, the python socket server issues a request
    internally to connect to port 2999 and passes all the data/socket information to port 2999.
    And similarly, any data returned from the service (server from first problem of C++
    programming question) to Python socket program is returned all the way back to the client
    user which initially connected to port 3111. Here is how it looks:
    
    C++ Socket      ----->  Python Socket   ----->  Client User
    Server on port  <-----  Server on port  <-----
    2999                    3111
    
2.  Write a program that displays all the data packet that flows through the given network
    interface. For example, if network interface eth0 is selected, it displays all the incoming and
    outgoing packets through this network interface. While displaying a packet, showing
    incoming IP address, port, destination IP address and port is enough. You CANNOT use tools
    like netncat, nc or any other network tools.
    
1) cd CppCodes
   ./server
   
   cd PythonCodes
   python3 ServerClientInterface.py
   python3 Client3111.py
   
2) cd PythonCodes
   python3 PacketDecoder.py

