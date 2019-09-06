from sklearn import datasets
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score

iris = datasets.load_iris()
X = iris.data[:, [2, 3]]
y = iris.target
print('Class labels:', np.unique(y))

# トレーニングデータとテストデータに分割（全体の30%をランダムにテストデータにする）
# test_size : テストデータの割合
# random_state : Noneにすると毎回違うデータが生成されるが、整数をシードとして渡すと毎回同じデータが生成される。
# stratify : 層化サンプリング（https://bellcurve.jp/statistics/course/8007.html）
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1, stratify=y)

# 層化サンプリング結果の確認
print('Labels counts in y:', np.bincount(y))
print('Labels counts in y_train:', np.bincount(y_train))
print('Labels counts in y_test:', np.bincount(y_test))

# 特徴量を標準化する
sc = StandardScaler()
# トレーニングデータの平均と標準偏差を計算
sc.fit(X_train)
# 平均と標準偏差を用いて標準化
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)

# エポック数40、学習率0.1でパーセプトロンのインスタンスを生成
ppn = Perceptron(max_iter=40, eta0=0.1, random_state=1)
# トレーニングデータをモデルに適合させる
ppn.fit(X_train_std, y_train)

# テストデータで予測を実施
y_pred = ppn.predict(X_test_std)
# 誤分類のサンプルの個数を表示
print('Misclassified samples: %d' % (y_test != y_pred).sum())

# 正解率を表示
print('Accuracy: %.2f' % accuracy_score(y_test, y_pred))

# 各分類器に定義されているscoreメソッドで正解率を表示
print('Accuracy: %.2f' % ppn.score(X_test_std, y_test))
