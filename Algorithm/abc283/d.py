from collections import defaultdict

S = input()
X = []  # 中断した () を管理するリスト
Y = defaultdict(bool)   # a ～ z がすでに箱に入っているか管理
now = set() # 今見ている () の中身を管理

for s in S:
    if s == "(":    # 新しい () の登場にあわせて、今見ている () を X に格納
        X.append(now)
        now = set()
    elif s == ")":
        for k in now:   # 今見ている () の中身をキーに X を初期化
            Y[k] = False
        now = X.pop()   # 直前の () を取り出す
    else:
        if Y[s]:    # 被りを検出したら終了
            print("No")
            exit()
        Y[s] = True # s を使用済みに変更
        now.add(s)  # 今見ている () に s が存在することを記録
print("Yes")