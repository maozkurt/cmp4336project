import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import pandas as pd

n_clusters = 15
df = pd.read_csv('dataset.csv')

# scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df.drop(columns=['Address']))

# pca
pca = PCA(n_components=2)
points = pca.fit_transform(X_scaled)

# kmeans
kmeans = KMeans(n_clusters = n_clusters)
kmeans.fit(points)

centroids = kmeans.cluster_centers_
labels = kmeans.labels_

# plotting 
plt.figure(figsize=(6,5))
plt.scatter(points[:, 0], points[:, 1], c=labels, cmap='viridis', s=50, alpha=0.5)
plt.scatter(centroids[:, 0], centroids[:, 1], marker='*', s=200, c='r', label='Centroids')
plt.title('K-means Clustering')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
plt.show()
