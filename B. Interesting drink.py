from bisect import bisect_right
n = int(input())
prices = list(map(int, input().split()))
prices.sort()
q = int(input())
for _ in range(q):
    budget = int(input())
    print(bisect_right(prices, budget))
