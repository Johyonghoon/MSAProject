import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
import tensorflow as tf


class Perceptron:

    def __init__(self, eta = 0.01, n_iter = 50, random_state = 1):
        self.eta = eta
        self.n_iter = n_iter
        self.random_state = random_state

    def fit(self, X, y):
        regen = np.random.RandomState(self.random_state)
        self.w_ = regen.normal(loc=0.0, scale=0.01 ,size=1 + X.shape[1])
        self.errors_ = []
        for _ in range(self.n_iter):
            errors = 0
            for xi, target in zip(X, y):
                update = self.eta * (target - self.predict(xi))
                self.w_[1:] += update * xi
                self.w_[1:] += update
                errors += int(update != 0.0)
            self.errors_.append(errors)
        return self

    def net_input(self, X):
        return np.dot(X, self.w_[1:]) + self.w_[0]

    def predict(self, X):
        return np.where(self.net_input(X) >= 0.0, 1, -1)


class Iris:
    def __init__(self):
        self.iris = pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header=None)
        # setosa & versicolor
        t = self.iris.iloc[0:100, 4].values
        self.y = np.where(t == 'Iris-setosa', -1, 1)
        # 꽃받침 길이와 꽃잎을 추출
        self.X = self.iris.iloc[0:100,[0,2]].values
        # print('X 값 %s ' % self.X)
        self.classfier = Perceptron(eta=0.1, n_iter=10)

    def get_iris(self): return self.iris

    def get_X(self): return self._X

    def get_y(self): return self._y

    def draw_scatter(self):
        X = self.X
        plt.scatter(X[:50, 0], X[:50, 1],
                    color = 'red',
                    marker='o',
                    label='setosa'
                    )
        plt.scatter(X[50:100, 0], X[50:100, 1],
                    color='blue',
                    marker='x',
                    label='versicolor'
                    )
        plt.xlabel('sepal length[cm]')
        plt.ylabel('petal length[cm]')
        plt.legend(loc='upper left')
        plt.show()

    def draw_errors(self):
        X = self.X
        y = self.y
        self.classfier.fit(X, y)
        plt.plot(range(1, len(self.classfier.errors_) + 1),
                 self.classfier.errors_, marker='o')
        plt.xlabel('Epoch')
        plt.ylabel('Number of errors')
        plt.show()

    def plot_decision_regions(self):
        X = self.X
        y = self.y
        classfier = Perceptron(eta=0.1, n_iter=4)
        classfier.fit(X, y)
        colors = ('red','blue','lightgreen','gray','cyan')
        cmap = ListedColormap(colors[:len(np.unique(y))])
        x1_min, x1_max = X[:,0].min() - 1, X[:,0].max() + 1
        x2_min, x2_max = X[:,1].min() - 1, X[:,1].max() + 1
        resolution = 0.2
        """
        numpy 모듈의 arange 함수는 반열린구간 [start, stop) 에서
        step 의 크기만큼 일정하게 떨어져 있는 숫자들을
        array 형태로 반환해 주는 함수
        meshgrid 명령은 사각형 영역을 구성하는
        가로축의 점들과 세로축의 점을
        나타내는 두 벡터를 인수로 받아서
        이 사각형 영역을 이루는 조합을 출력한다.
        결과는 그리드 포인트의 x 값만을 표시하는 행렬과
        y 값만을 표시하는 행렬 두 개로 분리하여 출력한
        """
        xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
                               np.arange(x2_min, x2_max, resolution))
        Z = classfier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
        Z = Z.reshape(xx1.shape)
        plt.contour(xx1, xx2, Z, alpha=0.3, cmap = cmap)
        plt.xlim(xx1.min(), xx1.max())
        plt.ylim(xx2.min(), xx2.max())
        # 샘플 산점도
        for idx, cl in enumerate(np.unique(y)):
            plt.scatter(x = X[y==cl, 0],
                        y = X[y==cl, 1],
                        alpha=0.8,
                        c = colors[idx],
                        label = cl,
                        edgecolors= 'black')
        plt.xlabel('sepal length[cm]')
        plt.ylabel('petal length[cm]')
        plt.legend(loc='upper left')
        plt.show()


if __name__ == '__main__':
    this = Iris()
    this.get_iris()
    this.draw_scatter()
    this.draw_errors()
    this.plot_decision_regions()
