import math
import random
import time
from collections import deque

"""
絶対値
"""
abs(-2)  # 2

""" 
三角関数
"""
math.sin(0)  # 0.0
math.cos(0)  # 1.0
math.tan(0)  # 0.0

"""
文字列
"""
s1, s2 = 'abc', 'def'
s1[1]  # b
s1 + s2  # abcdef
len(s1)  # 3
s1[1:3]  # bc

"""
最小値・最大値
"""
min(1, 2)  # 1
max(1, 2)  # 2

"""
値の交換
"""
a, b = 1, 2
a, b = b, a  # a:2 b:1

"""
最大公約数
"""
math.gcd(6, 4)  # 2

"""
乱数
"""
# 0.0～1.0の範囲
random.random()
# 範囲指定
random.uniform(100.0, -100.0)

"""
時間計測
"""
t0 = time.time()
t1 = time.time()
# print('Cal time:{}'.format(t1-t0))

"""
配列を逆順に並び替え
"""
l = [1, 2, 3, 4, 5]
l.reverse()  # l = [5, 4, 3, 2, 1]
l1 = [1, 2, 3, 4, 5]
l2 = l1[::-1]  # l2 = [5, 4, 3, 2, 1]

"""
ソート
"""
l = [2, 4, 5, 3, 1]
l.sort()  # l = [1, 2, 3, 4, 5]
l.sort(reverse=True)  # l = [5, 4, 3, 2, 1]

"""
動的配列 (C++ vector)
"""
l = list()
# 末尾に要素を追加
l.append(1)  # l = [1]
l.append(2)  # l = [1, 2]
# 末尾の要素を削除
l.pop()  # l = [1]

"""
Stack
"""
l = list()
# 末尾に要素を追加
l.append(1)  # l = [1]
l.append(2)  # l = [1, 2]
# 末尾の要素を削除
l.pop()  # l = [1]

"""
Queue
"""
q = deque()
q.append(1)  # q = [1]
q.append(2)  # q = [1, 2]
q.popleft()  # q = [2]

"""
Priority Queue
"""
