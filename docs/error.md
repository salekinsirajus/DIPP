The protocol has the following error reporting mechanism. The error report
will contain both numeric and human readable components. 

Errors and reports are divided into the following broad categories:

# 1 : Success
    This is not an error category. Reports starting with 0 indicates the 
    exchange was successful.
    1000 = Success Registration
        This status code is sent after a device is able to register to the 
        network. (The packet might contain necessary information relating
        registration)
    1001 = Connected to Host 
        Whenever a connection is initiated, and it is successful, and the 
        initiator gets this status code is sent  as confirmation, and that 
        host can move on carry out other network activities.

# 2 : Errors on the network
    2001 = Host unreachable
        When a device is registered in the network but is unable to receive 
        or send data, i.e., could be powered off.
    2002 = Address Error (communicated from TCP)
        When the IP or the port address is not correct
    2003 = Host Not Registered
    2004 = Firewall blocked?
    2005 = Authentication Failure
        When trying to register but didn't get the password or key right

# 3 : Error with the content
    3001 = Requested content not found
    3002 = Invalid Request
    3003 = Service Not Implemented
    2004 = Refused servic/content
