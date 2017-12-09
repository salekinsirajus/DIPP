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

Message Structure
    Instead of deciding these are contents a node has to provide, we will leave
    that decision to the implementers/developers. However, there should be nice
    modular structue for doing that. Basically, we will provide a structure,
    and the implementers are free to implement whatever they want. We can also
    provide frequently used services.

    Each node can provide some contents/service to the participating nodes. 
    For example, a humidity sensor node would definitely provide the services
    that will send the reading of current humidity in the room.


            REQ | SERVICE | READING | HUMIDITY SENSOR
    However, every node is required to provide the following services:

            REQ | SERVICE | LIST
        This send an available list of services provided by the node
            REQ | SERVICE | 

Message Exchange Pattern:
    So far, we designed our protocol around request-response pattern. Although
    this model very prevalent in client-server interaction based protocol, we
    found this to be useful for our purposes. However, we also considered 
    publisher-subscriber scenario, which might be efficient for power-
    constrained sensor devices. (We need to figure out how these two live in 
    harmony and peace)

    Let's talk about each models, and compare it against the requirement of 
    our protocol.

    * Request-Response: It can be synchronus and asynchronus. Synchronus means
    that after sending a request, the reciever has to respond within a certain
    timelimit. Asynchronus means there is no time out for the request, and the
    responder can respond at a later time. Now, it seems that for our purposes,
    asynchronus should work fine. Adding time limit adds more complexity.

    However, as we plan to utilize the local resources more effectively, once 
    a connection is established, it is not necessary to require a reply with
    every response, especially on top of TCP.

    * Fire-and-Forget/: There are situations when only sending a message might
    be all the devices need to do. There is no requirement for reply within a
    timelimit. The format for such messages could be FNF | <Message Body>
    (also known as DATAGRAM)

    * Push-Pull: Push-Pull could be seen as the opposite of request-response.
    In req-res model, initiating host typically wants to receive some type of
    contents, whereas in push-pull, it is similar to sending some data to a
    device, asking something to do with it, and getting the result back.
    (However we need to see if this can be modeled after a client response 
    scenario)
    
Encoding: DIPP is a simple text-based protocol. Most of the devices that would
    use this protocol will exchange short amount of data, so using a text-based
    protocol seemed to be the appropriate choice. Human rreadability was also
    another important factor in our consideration. UTF-8 with MIME?

Security: We are considering using TLS/SSL. (or use one of the robust
    but lighweight security systems)

Authentication: authentication in a peer-to-peer network is a difficult task to
    accomplish, due to the absence of a central server. We also needed to keep
    the energy requiremnts and cost-effectiveness in mind before choosing an
    authentication protocol. 
