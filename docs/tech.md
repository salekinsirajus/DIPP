Technical Challenges:

    (We will list the technical challneges/questions faced as we
    work through the project.)

    Routing/Registering:
        1. Do we need to keep a port open for listening at all nodes
        
            We certainly can, but looking at it from power-constraint
            perspective, but necessarily a great idea to implement. 
            Although, it might be okay to keep a listening port open 
            all the time, if it doesn't drain the electricity too much.
            On nodes like that, we can implement pub-sub functionality.
            However, it does not hurt keeping the code available in the
            machine to run a sever. If we decide to go along with the 
            idea of keeping port open (meaning have the server.py running
            all the time, it is important we check how much storage and
            memory it is taking up. 

        2. How do we adress NAT issues? Do we only care about devices using
            the same router, or different ones?

            Since every machine has a list of devices it keeps track of, we
            we can extract these data from the TCP packet? or from the nodes
            themselves? 

            Option 1: if we ask the nodes to explicitly provide their address
                    we are going to run into trouble when two device are
                    connected through different routers. (This takes us to
                    our next question)

            Option 2: We can extract the IP and port addresses using from the
                    TCP packets. An IP from the same network will be identified
                    and reachable since it is in the same network. And an IP
                    address that was tanslated through NAT should give us a
                    public IP, which is translated by their router and we don't
                    worry about that.


        3. Is this network private, or the nodes are publicly addressable?
            Google: peer to peer public ip
            Google: IoT should they have public or private IP
            Google: gateway in an IoT network
            Google: private iot network

        4. Comment: once a connection is established, both hosts can send 
            bi-directional data. It only matters when initiating the connection
            : who can/should initiate it.
            In pub-sub sceanrios, the sensor initiate the subscribers (usually
            the servers) for connection. This scenario is pretty much how it
            traditional connections work
            In Req-response scenarios, when the client initiates the connection 
            to the server, it is fine. However, when server initiates the
            connection, that's when it becomes a problem. In an IoT network, 
            this could be a great addition though: theoritically, any machine
            can directly talk to any other machine. (does ipv6 provides a 
            solution to this problem? Probably not)
