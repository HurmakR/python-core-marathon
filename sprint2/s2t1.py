def double_string(data):
    l=[]
    for i in set(data):
        for j in data:
            if i + j in data :
                l.append(i + j)
    counter = 0
    for k in data:
        if k in l:
            counter += 1
        
    return counter