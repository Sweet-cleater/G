N, M = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

out = []
for b in B:
    out.append(A[b-1])
print(sum(out))