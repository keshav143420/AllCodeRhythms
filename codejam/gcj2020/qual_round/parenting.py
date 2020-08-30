test_cases = int(input())
for test_case in range(test_cases):
    temp1 = []
    temp2 = []
    cameron_activity = 0
    jamie_activity = 0
    str_arr = ['C']
    final = ''
    N = int(input())
    for i in range(N):
        temp1.append(list(map(int, input().split())))
    temp2 = temp1.copy()
    temp1.sort()
    cameron_activity = temp1[0][1]
    for i in range(1, N):
        if temp1[i][0] >= cameron_activity or temp1[i][0] >= jamie_activity:
            if temp1[i][0] >= cameron_activity:
                str_arr.append('C')
                cameron_activity = temp1[i][1]
            else:
                str_arr.append('J')
                jamie_activity = temp1[i][1]
        else:
            final = 'IMPOSSIBLE'
    temp3 = []
    if final != 'IMPOSSIBLE':
        for i in range(N):
            for j in range(N):
                if temp2[i] == temp1[j] and j not in temp3:
                    final = final + str_arr[j]
                    temp3.append(j)
                    break
    print("Case #{}: {}".format(test_case + 1, final))
