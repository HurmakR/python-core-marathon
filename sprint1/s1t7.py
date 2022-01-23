def Cipher_Zeroes(N):
    point = 0
    for i in N:
        if i in ['0', '6', '9']:
            point += 1
        elif i == '8':
            point += 2
    if point % 2 == 0 and point > 0:
        return bin(point - 1)[2:]
    elif point % 2 != 0 and point > 0:
        return bin(point + 1)[2:]
    else:
        return bin(point)[2:]
