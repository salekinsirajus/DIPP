"""import csv

qeuery = ['deliver', 'tempSensor']
with open('dummy_data_index.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['owner'] == qeuery[1]:
                print ("copy the file over the network")
#                s.sendall('deliver'.encode('utf-8'))
                filename = row['file_loc']
                print (filename)
"""
# Doing a bunch of request-response scenario
import platform

def res(req):
    node = platform.node()
    machine = platform.machine()
    os = platform.system()
    neighbors = ['10.10.10.11', '10.10.11.11']
    return {
        'name': 'nestThermostat',
        'current': 65,
        'address': '10.10.10.1',
        'machine':machine,
        'os':os,
        'ip': node,
        'nodeType': 'Node',
        'storage': 'small',
        'memory': 'small',
        'neighbors':neighbors,
        'passwod': 'torMayereBaap',
        'status': ['active', 'down']
    }.get(req, "Invalid")
