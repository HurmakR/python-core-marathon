def kthTerm(n, k):
    sum_list = [1]
    temp_list = []
    counter = 1
    while len(sum_list) <= k:
        temp_list.append(n**counter)
        for i in sum_list:
            temp_list.append((n**counter) + i)
        sum_list.extend(temp_list)
        temp_list = []
        counter += 1
    return sum_list[k - 1]