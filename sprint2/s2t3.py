import re

def figure_perimetr(data):
    points=re.findall(r'([A-Z]{2})(\d):(\d)',data)
    res=0
    pairs=[]
    for i in points:
        for j in points:
            if (i[0][0] in j[0]  or i[0][1] in j[0]) and i[0] != j[0] and j[0] + i[0] not in pairs:
                pairs.append(i[0] + j[0])
                res+= ((int(j[1])-int(i[1]))**2+(int(j[2])-int(i[2]))**2)**(1/2)
    return res