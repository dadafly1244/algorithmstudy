import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

mindata =min(data)
maxdata = max(data)

print(mindata, maxdata)