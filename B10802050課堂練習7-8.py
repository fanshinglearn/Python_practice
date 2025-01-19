A = {'馬林魚':'3勝4敗', '洋基':'5勝3敗', '天使':'4勝3敗', '道奇':'4勝4敗'}
B = {'馬林魚':'3勝4敗', '太空人':'5勝4敗', '洋基':'5勝3敗', '天使':'4勝3敗', '金鶯':'4勝5敗'}

for b in iter(B):
    if b not in A:
        A[b] = B[b]
B.clear()
print(A)
print(B)

for b in iter(B):
    A.setdefault(b,B[b])
B.clear()
print(A)
print(B)