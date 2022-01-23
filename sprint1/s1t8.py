def studying_hours(a):
    sub_lenght = 1
    subs_list = []
    for i in range(len(a) - 1):
        if a[i] <= a[i + 1]:
            sub_lenght += 1
        else:
            subs_list.append(sub_lenght)
            sub_lenght = 1
    subs_list.append(sub_lenght)
    return max(subs_list)
