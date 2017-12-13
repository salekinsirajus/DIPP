from payloadParser import parse_payload

# Deals with push methods

def push(method, payload):
    # what do I do with the data?
    # make it available for some apps
    # return them??
    if method == 'PAK':
        print("PAK--making acks")
        tuples = parse_payload(method, payload)
        ack_msg = "ACK"
        print ("returned from payload parser ", tuples)
        for t in tuples:
            "assigning ack/nack to fields" 
            field = t[0]
            val = t[1]
            # for now, we ack everything
            ack_msg = ack_msg + " " + field + ":" + "ACK"
        ack_msg = ack_msg + "\r\n" #Adding the frame delimiter
        return ack_msg
    elif method == 'PNF':
        print ("OK recieved data. GO home and sleep")
        tuples = parse_payload(method, payload)
        return 
    elif method == 'ACK':
        print ("Thanks for the ACK. I can sleep now")
        tuples = parse_payload(method, payload)
        return
    return 
