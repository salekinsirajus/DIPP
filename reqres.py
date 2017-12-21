# This module implement request-response methods.
from payloadParser import res, parse_payload

def req_res(method, payload):
    # If it's a REQ field, try match with the listed things
    # Come up with a response, return the response to caller

    # if it's RESponse field, print thanks. (or get me out of the loop?)
    # (if implemented stateful part)

    if method == 'REQ':
        print ("Preparing response")
        fields_only = parse_payload(method, payload)
        response_msg = "RES"
        for field in fields_only:
            value = res(field)
            response_msg = response_msg + " "+ field + ":"+value

        response_msg = response_msg + "\r\n" #Adding the frame delimiter
        return response_msg
        
    elif method == 'RES':
        print ("No response. Can ask question")
        tuples = parse_payload(method, payload)
        return "3006-Illegal-Command-Send-REQ\r\n"
    else:
        print ("Not part of request response model")
        return "3007-Unrecognizable Method" 

