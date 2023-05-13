def pick_peaks(arr):
    if len(arr) == 0:
        return {'pos':[], 'peaks':[]}
    lst = [(0,arr[0])]
    for i in range(1,len(arr)):
        if arr[i] != arr[i-1]:
            lst.append((i,arr[i]))
    pos = []
    peaks = []
    for i in range(1,len(lst) -1):
        if (lst[i][1] > lst[i+1][1]) and (lst[i][1] > lst[i-1][1]):
            pos.append(lst[i][0])
            peaks.append(lst[i][1])
    return {'pos':pos, 'peaks':peaks}

