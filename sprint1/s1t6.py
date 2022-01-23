def order(a):
    if a == sorted(a, reverse = True):
        return('descending')
    elif a == sorted(a):
        return('ascending')
    else:
        return('not sorted')