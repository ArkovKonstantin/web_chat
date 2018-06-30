def bar(*args):
    try:
        a, b = args
    except ValueError:
        a = args[0]
        b = ''
    print('a = ', a,'b = ', b)


bar(1)