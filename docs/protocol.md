Sections:
    1. Basic Structure
    2. Scope: what's covered here what is not
    3. Registration
    4. Message Exchange
    5. Message Structure
    6. Encoding
    7. Security
    8. Privacy/Gateway to HTTP

Basic Structure:
    The basic structure of IOTP2P is that it enables message transfer 
    between two hosts. It allows full duplex communication (?) between
    any two participating hosts. We follow both request-response and 
    publisher-subscriber scenarios. 

        +----------+                        +-------+
        | Host     |<---------------------->| Host  |
        +----------+                        +-------+
    
    Depending on the type of the hosts, the functionalities of a host
    vary, and what type of communication would be successfull. 
    We categorize hosts in the following categories, based on their micro-
    processor or microconotroller, and sotrage. A design constraint for IoT
    devices is that they are heterogeneous, and comes in wildly different
    configurations.

Message Exchange Pattern:
    So far, we designed our protocol around request-response pattern. Although
    this model very prevalent in client-server interaction based protocol, we
    found this to be useful for our purposes. However, we also considered 
    publisher-subscriber scenario, which might be efficient for power-
    constrained sensor devices. (We need to figure out how these two live in 
    harmony and peace)
