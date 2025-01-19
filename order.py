def order(dishes):
    x = input('%s : %s、%s及%s三選一 '%(dishes[0], dishes[1], dishes[2], dishes[3]))
    print('你點的%s是 : %s\n'%(dishes[0], dishes[int(x)]))
    return int(x)