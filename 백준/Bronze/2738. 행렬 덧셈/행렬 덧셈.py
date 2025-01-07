row_list,cols_list = [],[]
N, M = map(int, input().split())

for i in range(N):
    row = list(map(int, input().split()))
    row_list.append(row)

for i in range(N):
    cols= list(map(int, input().split()))
    cols_list.append(cols)
    
for i in range(N):
    for j in range(M):
        print(str(row_list[i][j] + cols_list[i][j])+" ", end ="")
    print()