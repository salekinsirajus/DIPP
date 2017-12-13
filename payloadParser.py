import platform
import random # to simulate a temp value

def res(req):
    """ 
    returns responses based on the query.
    fieldnames are case insensitive. 
    """
    req = req.upper()
    temp = random.randint(50,80)
    temp = str(temp)
    return {
        'DEVICENAME': 'nestThermostat',
        'DEVICETYPE': 'sensor',
        'READINGTYPE': 'temperature',
        'READINGUNIT': 'Fahrenhite',
        'READINGCURRENT': temp,
        'ISFULLNODE': 'False',
        'ISALIVE': 'True',
    }.get(req, "3004-Unrecognized-Field")

# We need to parse two different type of things
# field<sp>field 
# and
# field:val<sp>field:val

def parse_payload(method, payload):
    # Be consistent what you want in payload.
    # After that, we can dissect the string and parse
    if method == 'REQ':
        print ("REQ method, match it with response")
        fields_only = payload.split()
        return fields_only

    elif method in ['PNF', 'PAK', 'ACK', 'RES']:
        # print ("f:v pairs")
        fv_pairs = payload.split()
        fv_tuples = []
        for pair in fv_pairs:
            (f,v) = pair.split(':')
            fv_tuples.append((f,v))
        #print (fv_tuples)
        return fv_tuples

    else:
        print ("not a valid message format")
        return None
#    try:
#        print(fields_only)
#        print(fv_pairs)
#    except:
#        print ("lol try block's wrong")
