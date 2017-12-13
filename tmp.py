#Doing a bunch of request-response scenario
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
