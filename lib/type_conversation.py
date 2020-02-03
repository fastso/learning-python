# 型変換Utility


# str -> List[int]
s = '1234'
l = [int(_) for _ in list(s)]
# l = [1, 2, 3, 4]

# List[int] -> str
l = [1, 2, 3, 4]
s = ''.join(map(str, l))
# s = '1234'

# List -> Dict
# リストlの値をディクショナリーのキーに変換
l = ['key1', 'key2', 'key3']
v_l = [0] * len(l)
d = dict(zip(l, v_l))
# d = {'key1': 0, 'key2': 0, 'key3': 0}
