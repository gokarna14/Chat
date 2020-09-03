def add(filename, data = ''):
    fr = open(filename, 'a+')
    if data == '':
        while 1:
            q = input(f'Enter for {filename} : ')
            if q != '':
                fr.write('\n' + q.lower())
            else:
                break
    else:
        fr.write('\n' + data)
    fr.close()
    if not 'learn' in filename:
        filter_data(filename)


def filter_data(filename):
    write_list = []
    fr = open(filename, 'r+')
    l = fr.read().split('\n')
    for i in l:
        if i not in write_list and i != '':
            write_list.append(i)
    fr.close()
    fw = open(filename, 'w+')
    fw.write('\n'.join(write_list))
    fw.close()