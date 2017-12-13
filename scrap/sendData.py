from client import *
import csv

def sendBulkData(destination, qeuery):

    # destination is a tuple of address and port
    while not isinstance(destination, tuple):
        return ("Inavlid address pair. (IP and Port)")

    try:
        isinstance(destination, tuple)
        s = initSocket('SOCK_STREAM')
        s = connectNode(s, destination[0], destination[1])
    
    except Exception as e:
        print ("Connection error {}".format(e))
    
    print (qeuery[0], qeuery[1])
    if qeuery[0] == 'deliver':
        print ("we need to send some data")
    # run qeuery[1] to find out what kind of data do we need
    # We will use the csv file to read what's in the 'index' file
    with open('dummy_data_index.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['owner'] == qeuery[1]:
                print ("copy the file over the network")
                cmd = "deliver"
                s.send(cmd.encode('utf-8'))
                filename = row['file_loc']
             
                f = open(filename, 'rb')
                l = f.read(1024)
                while (l):
                    s.send(l)
                    print ('sent ', repr(l))
                    l = f.read(1024)
                f.close()
        
    print ("Successfully delievered data for {}".format(qeuery))
    return 0
    
print (sendBulkData(('127.0.0.1', 9999), ['deliver', 'tempSensor']))
