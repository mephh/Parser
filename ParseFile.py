import os


def parse_log():
    for x in os.listdir('c:\users\bastrza\Desktop\Z18_parser'):
        if os.path.isfile(x): print x
parse_log()


    # filter(lambda x: os.path.isfile(x), os.listdir('.'))
    # print filter
    # with open(, 'w') as infile:
    #     for line in infile:
    #         line.strip()
    #         serial = []
    #         if line.startswith('SERIAL No ='):
    #             serial.append(line[:12])
    #         print line
