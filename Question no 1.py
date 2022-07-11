L = [9, 2, 1, 7, 5]
print(L)

i = 1
while i < len(L):
    key = L[i]
    j = i - 1
    while j >= 0 and key < L[j]:
        L[j + 1] = L[j]
        j = j - 1
    else:
        L[j + 1] = key
        i = i + 1
else:
    print(L)
