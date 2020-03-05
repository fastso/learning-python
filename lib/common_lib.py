import math
import random
import time
from collections import deque
import heapq
from collections import defaultdict
from collections import OrderedDict
import bisect
import itertools

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
優先度付きキュー
"""
l = [1, 6, 8, 0, -1]
# リストを優先度付きキューへ
heapq.heapify(l)  # l = [-1, 0, 8, 1, 6]
# 最小値の取り出し (最大値は各要素にかける-1で取る)
a = heapq.heappop(l)  # a = -1 l = [0, 1, 8, 6]
# 要素の挿入
heapq.heappush(l, -2)  # l = [-2, 0, 8, 6, 1]

"""
連想配列
dict (C++ map)
"""
d = {'x': 1, 'y': 1}
d['x']  # 1
d['z'] = 1  # d = {'x': 1, 'y': 1, 'z': 1}

# キーがない時は、自動的に0をセットしてくれるのがデフォルト辞書
seed = ['apple', 'orange', 'banana', 'orange', 'banana', 'apple', 'apple', 'apple']
md = defaultdict(int)
for key in seed:
    md[key] += 1
# md = {'apple': 4, 'orange': 2, 'banana': 2}

# キーの挿入順の保証の辞書
od = OrderedDict()

"""
二分探索 
bisect (C++ lower_bound)
"""
a = [1, 2, 3, 3, 3, 4, 4, 6, 6, 6, 6]
a.sort()  # aがソート済リスト
index = bisect.bisect_left(a, 3)  # 2 最も左(前)の挿入箇所が返ってきている
a.insert(index, 3)  # a = [1, 2, 3, 3, 3, 3, 4, 4, 6, 6, 6, 6]

bisect.bisect_right(a, 3)  # 5   bisectはbisect_rightのalias

# 探索範囲を絞り込む
a = [1, 2, 3, 3, 3, 0, 0, 0, 0, 0, 0]
index = bisect.bisect_left(a, 3, 0, 5)  # 2

# insort_left(a, x) と a.insert(bisect.bisect_left(a, x)) と同じ
a = [1, 2, 3, 3, 3, 4, 4, 6, 6, 6, 6]
bisect.insort_left(a, 3)  # [1, 2, 3, 3, 3, 3, 4, 4, 6, 6, 6, 6]

bisect.insort_right(a, 3)  # insortはinsort_rightのalias

"""
集合
set
"""
s = {'apple', 'melon', 'peach'}
# 集合sに要素を追加
s.add('banana')  # s = {'apple', 'melon', 'peach', 'banana'}
# 集合の要素を削除（要素が存在しない場合はエラー）
s.remove('banana')  # s = {'melon', 'apple', 'peach'}
# s.remove('banana')  # エラー発生
# 集合の要素を削除（要素が存在しなくてもエラーが発生しない）
s.discard('banana')

"""
2つの異なる型を一つの変数で持つ
(C++ pair)
"""
pairs = [("a", 1), ("b", 2), ("c", 3)]
for a, b in pairs:
    continue
    print(a, b)

"""
3つの異なる型を一つの変数で持つ
(C++ tuple)
"""
tuple = [("a", 1, 1.0), ("b", 2, 2.0), ("c", 3, 3.0)]
for a, b, c in tuple:
    continue
    print(a, b, c)

"""
assert
"""
n = 10001
# assert n < 10000, 'error message'

"""
count
"""
l = [1, 2, 3, 4, 1, 2, 3, 1, 2, 1]
l.count(3)  # 2

"""
index
(C++ find)
"""
l = [1, 2, 3, 4, 1, 2, 3, 1, 2, 1]
l.index(3)

"""
全列挙
(C++ next_permutation)
"""
# 順列の列挙（3つの中2つを選ぶ順列）
nums = [1, 2, 3]
for balls in itertools.permutations(nums, 2):
    continue
    print(balls)

# 順列の列挙
nums = [1, 2, 3]
for balls in itertools.permutations(nums):
    continue
    print(balls)

# 組合せの列挙（3つの中2つを選ぶ組合せ）
nums = [1, 2, 3]
for balls in itertools.combinations(nums, 2):
    continue
    print(balls)

# 1, 2, 3と書かれた玉が入った袋から、2つの玉を取り出す。ただし取り出した玉はまた袋に戻す (重複順列)
nums = [1, 2, 3]
for balls in itertools.product(nums, repeat=2):
    continue
    print(balls)

# 1, 2, 3と書かれた玉が2セット入った袋から、2つの玉を区別なく同時に取り出す（重複組合せ）
nums = [1, 2, 3]
for balls in itertools.combinations_with_replacement(nums, 2):
    continue
    print(balls)

# 2つの集合の直積を取る
signs = ['a', 'b', 'c']
nums = [1, 2, 3]
for pairs in itertools.product(signs, nums):
    continue
    print(pairs)

"""
整数 x を二進数で表したとき、1 であるようなビットの個数を返す
(C++ __builtin_popcount)
"""
bin(5).count('1')  # 2

"""
(C++ bitset)
Pythonでの代替は見つかりません
"""


