def check_code(part_SN):
    with open ('config.dat', 'r') as infile:
        for line in infile:
            line.strip()
            if line[:8] == part_SN:         # from 1st to 8th char
                code = line[9:]             # from 9th char
                return code
            else:
                print('mm')








x = '12345678'
check_code(x)
