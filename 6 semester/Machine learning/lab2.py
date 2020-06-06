import torch
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA


def PCA_sklearn(X):
	"""Обчислення PCA за допомогою sklearn"""
	pca = PCA(n_components=2)
	pca.fit(X)

	print('sklearn')
	print(pca.components_)
	print(pca.explained_variance_)
	print(pca.mean_)
	print()

	return {'components': pca.components_,
			'explained_variance': pca.explained_variance_,
			'mean': pca.mean_}


def PCA_pytorch(X, k=2, center=True):
	"""Обчислення PCA за допомогою PyTorch"""
	n = X.size()[0]
	ones = torch.ones(n).view([n, 1])
	h = ((1 / n) * torch.mm(ones, ones.t())) if center else torch.zeros(n * n).view([n, n])
	H = torch.eye(n) - h
	X_center = torch.mm(H.double(), X.double())
	u, s, v = torch.svd(X_center)
	v[1:]=v[1:]*-1
	components = v[:k].numpy()
	explained_variance = torch.mul(s[:k], s[:k]) / (n - 1)
	explained_variance = explained_variance.numpy()
	mean = [X[:, 0].mean().numpy().item(), X[:, 1].mean().numpy().item()]

	print('PyTorch')
	print(components)
	print(explained_variance)
	print(mean)
	print()

	return {'components': components,
			'explained_variance': explained_variance,
			'mean': mean}


def draw_vector(v0, v1, ax=None):
	ax = ax or plt.gca()
	arrowprops = dict(arrowstyle='->', linewidth=2, shrinkA=0, shrinkB=0)
	ax.annotate('', v1, v0, arrowprops=arrowprops)


def plot_data(X, explained_variance, components, mean):
	"""Візуалізація PCA"""
	plt.scatter(X['total_bill'], X['size'], alpha=0.2)
	for length, vector in zip(explained_variance, components):
		v = vector * 3 * np.sqrt(length)
		draw_vector(mean, mean + v)
	plt.xlabel('total_bill')
	plt.ylabel('size')
	plt.axis('equal')
	plt.show()


# ініціаліція датасету
tips = sns.load_dataset("tips")  # 'total_bill', 'smoker', 'time', 'size'
X = tips[['total_bill', 'size']]

# обчислення PCA за допомогою sklearn
res_sklearn = PCA_sklearn(X)
plot_data(X, res_sklearn['explained_variance'], res_sklearn['components'], res_sklearn['mean'])

# обчислення PCA за допомогою PyTorch
res_pytorch = PCA_pytorch(torch.tensor(X.values))
plot_data(X, res_pytorch['explained_variance'], res_pytorch['components'], res_pytorch['mean'])

# знешумлення
noisy = np.random.normal(X, 0.25)
plt.scatter(noisy[:, 0], noisy[:, 1], marker='>', c='g', alpha=0.5)
pca = PCA(1)
pca = pca.fit(noisy)
components = pca.transform(noisy)
filtered = pca.inverse_transform(components)
plt.scatter(filtered[:, 0], filtered[:, 1], c='r', alpha=0.5)
plt.show()
