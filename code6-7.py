scores1 = [80,40,50]
scores2 = [80,40,50]
print(f"scores1の先頭要素は{scores1[0]}")
print(f"scores2の先頭要素は{scores2[0]}")

print("scores2の中身を書き換えます")
scores2 = scores1

print("scores1の先頭要素を90に書き換えます")
scores1[0] = 90
print(f"90を代入したscores1の先頭要素は{scores1[0]}")
print(f"90を代入していないscores2の先頭要素は{scores2[0]}")