n, m = map(int,input().split())

result =0

for i in range(n):
    data= list(map(int, input().split()))
    min_num = 10001
    for a in data:
        min_num = min(min_num,a)
    result = max(result, min_num)    