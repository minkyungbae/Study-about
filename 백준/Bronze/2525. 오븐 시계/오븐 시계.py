h, m =map(int,input().split())
cooktime = int(input())
h += cooktime //60
m += cooktime %60
if m >= 60:
    h += 1
    m -= 60
    
if h >= 24:
    h -= 24
print(h,m)