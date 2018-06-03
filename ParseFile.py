import os
log_items = dict(datetime = 'dateandtime', serial = [], status = 'passorfail', faults=[])
local_dir = 'c:\\bastrza'
month = {'January':'01', 'February':'02', 'March':'03', 'April':'04', 'May':'05',
'June':'06', 'July':'07', 'August':'08', 'September':'09', 'October':'10', 'November':'11', 'December':'12'}
# office_dir = 'c:\users\\bastrza\Desktop\Z18_parser'
def parse_log():
    filenames = []
    filenames = os.listdir(local_dir)
    # print(filenames)
    # for each in filenames:
        # with open(os.path.join(local_dir, each), 'r+') as infile:
    with open('20180508_2246.log', 'r+') as infile:
    #     for line in infile:
    #         line = line.strip()
    #         if line.startswith('DATE'):
    #             dateline = line.split(' ')
    #             log_items['datetime'] = (dateline[7]+(month.get(dateline[3]))+dateline[5]+'_'+dateline[6].replace(':','_'))
    #         i=0
    #         if line.startswith('SERIAL No'):
    #             snline = line.split('=')
    #             log_items['serial'].append(snline[1])
    #             i+=1
    #         # if line.startswith('BOARD'):
    # print(log_items)

        tfile = []
        for line in infile:
            line = line.strip()
            tfile.append(line)
        enumerate(tfile)

        print(list(enumerate(tfile)), end='')
parse_log()
