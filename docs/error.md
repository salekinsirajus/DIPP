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
    

# 3 : Error with the content
    200 = Requested content not found
    201 = Invalid Request

