from reqres import req_res
from pushModel import push

def reg(method, msg):
    print ("register this thing")
    return "some res"

def method_parser(decoded_msg):
    """ This is a common parser to parse any message that comes through 
        After figuring out the method line, it then calls the appropriate
        messaging model. """

    print("common parser :",decoded_msg)
    # extracting the method field i.e., first three chars of msg
    method = decoded_msg[:3]
    # payload is things after the first three chars
    payload = decoded_msg[3:]   
    # call the message patterns and let them deal with it.
    if method == 'PAK':
        # PAK has return msg
        return push('PAK',payload) 
    elif method == 'ACK':
        return push('ACK',payload) 
    elif method == 'PNF':
        return push('PNF',payload) 
    elif method == 'REQ':
        return req_res('REQ', payload) 
    elif method =='RES':
        return req_res('RES', payload) 
    elif method == 'REG':
        print ("REG method")
        return "registration"
    else:
        print("Method field does not match. Discard?")
    return None

