# 型変換Utility

# n進数 -> 10進数
int('1101', 2)  # 2進数 -> 10進数
int('700', 8)  # 8進数 -> 10進数
int('FE', 16)  # 8進数 -> 16進数

# 10進数 -> n進数
bin(23)  # 10進数 -> 2進数 '0b10111'
oct(23)  # 10進数 -> 8進数 '0o27'
hex(23)  # 10進数 -> 16進数 '0x17'

# str -> ascii
ord('A')  # 97

# ascii -> str
chr(65)  # 'A'

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
