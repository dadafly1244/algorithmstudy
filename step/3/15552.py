import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
  a, b = map(int, input().split())
  print( a + b)

#https://www.acmicpc.net/problem/15552