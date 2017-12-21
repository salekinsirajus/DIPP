# Decentralized IoT Peer-to-Peer Protocol (DIPP)

## Peer to Peer for IoT devices
This is the software implementation for a peer to peer network aimed at 
Internet of Things (IoT) devices.

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1098483.svg)](https://doi.org/10.5281/zenodo.1098483)

## Description:
This project is an implementation of Senior Capstone Experience for Computer
Science majors at Earlham College. The software accompanies a paper, which
is the primary deliverable. Since we are proposing a protocol that is geared
towards IoT devices, we will produce a sample app that can live in the network
and do it's job. This repository contains development codes. Bugs, incomplete
features are, therefore, expected occurance. We will possibly use this to host
project website as well. If you have any question/suggestion, please send me an email to 
ssalek14@earlham.edu

## How To
1. Clone this repo
2. Run a TCP/UDP server by:
    python core.py
3. Open a telnet connection:
    **for tcp**
    ```
    telnet 127.0.0.1 9999
    ```
    **for udp**
    ```
    netcat -uv -u 127.0.0.1 9998
    ```
4. Send a sample query over tcp:
    REQ deviceName
or
    REQ currentReading

## Progress:
1. Can receive push messages, i.e., PAK, PNF and respond with ACK messages
2. Can receive and process REQ messages and resond back with RES.

## ToDo:
- [x] Produce a state diagram
- [x] Add more literature into the first draft of the paper
- [ ] Enforce state in REQ-RES model
- [ ] Provide client functions
- [ ] Provide standard API functions for both models
