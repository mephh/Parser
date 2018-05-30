import os
from ftplib import FTP
address = [
    '10.72.246.54',
    '10.72.246.59',
    '10.72.246.55',
    '10.72.246.56',
    '10.72.246.57',
    '10.72.246.58'
]
path = ['10.72.246.58']


for item in path:
    print("actually in: "+item)
    ftp = FTP(item, 'root', '1234')

    ftp.cwd('c\\bastrza')
    listing = []
    ftp.retrlines('LIST', listing.append)
    names = []
    for each in listing:
        separated = each.split(' ')
        names.append(separated[-1])
    names.remove('123')
    print names

    for each in names:
        print each
        local_filename = os.path.join(r"c:\users\bastrza\Desktop\Z18_parser", each)    #path to each ftp file
        lf = open(local_filename, "wb")                                     #creating local file with same name as file on ftp
        ftp.retrbinary("RETR "+each, lf.write, 1024)                        #downloading file and writing its data to a local file using 1024byte blocks
        lf.close()
        if os.path.isfile(local_filename):
            ftp.delete(each)
# #parsing time
