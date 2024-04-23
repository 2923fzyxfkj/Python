print('version 1.0')
print('author:冯治尧')
print('work:DNS server')
while 1:
    def a():
        print('1.New host 2.Search host 3.Exit')
        global a
        a = int(input('you choose:'))
    a()
    if a == 1:
        b = input('web name:')
        c = input('web host:')
        global d
        d = {b:c}
        a()
    if a == 2:
        e = input('web name:')
        if e in d:
            print(d[e])
        else:
            print('not found')
            a()
        a()
    if a == 3:
        exit()
    else:
        print('not choose')
        a()

