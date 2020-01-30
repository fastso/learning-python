# 型変換Utility

# List to Dict
# リストlの値をディクショナリーのキーに変換
l = ['key1', 'key2', 'key3']
v_l = [0] * len(l)
d = dict(zip(l, v_l))
