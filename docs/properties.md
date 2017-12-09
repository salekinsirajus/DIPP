# Protocol Mechanism and Properties 
We are using RFC 3117 as guide for designing our protocol. This document 
is regarded as "how-to" for protocol writing, and in our experience, it 
turns out to be a very usefull tool for bringing structue into the protocol
design process, from a pragmatic perspective.

## Mechanism
We are considering the following areas to figure out how our protocol works.

 [ ] Framing: how the begining and ending of a message is delimited
 [ ] Encoding: MIME, 822 (How a message is represented when exchanged
 [x] Reporting: Error Reporting: we are using 4-digit. Need to populate 
     the list now.
 [ ] Asynchrony: Initially thought of making it asynchronous, but it requires
     parallelism, and that requires 
