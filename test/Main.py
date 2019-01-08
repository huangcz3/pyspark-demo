# 生成多类单标签数据集
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets.samples_generator import make_blobs

center = [[1, 1], [-1, -1], [1, -1]]
cluster_std = 0.3
X, labels = make_blobs(n_samples=200, centers=center, n_features=2, cluster_std=cluster_std, random_state=0)
print('X.shape', X.shape)
print("labels", set(labels))

unique_lables = set(labels)
colors = plt.cm.Spectral(np.linspace(0, 1, len(unique_lables)))
for k, col in zip(unique_lables, colors):
    x_k = X[labels == k]
    plt.plot(x_k[:, 0], x_k[:, 1], 'o', markerfacecolor=col, markeredgecolor="k", markersize=14)
plt.title('= = = = = = = data by make_blob() = = = = = = =')
plt.show()
plt.s
