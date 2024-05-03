from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import pandas as pd
import matplotlib.pyplot as plt

# read dataset 
dataset = pd.read_csv('dataset.csv')

# scale the data
scaler = StandardScaler()
datascaled = scaler.fit_transform(dataset.drop(columns=['Address']))

# reduce number of dimensions using pca
pca = PCA(n_components=2)
datapca = pca.fit_transform(datascaled)

# dbscan
dbscan = DBSCAN(eps=0.01, min_samples=50)
dbscan.fit(datapca)

# labels
labels = dbscan.labels_
#print(labels)

# unique labels
uniquelabels = set(labels)
#print(uniquelabels)

# plot
plt.figure(figsize=(10, 6))
for label in uniquelabels:
    if label == -1:
        # noise points
        color = 'black'
    else:
        # coloring
        color = plt.cm.jet(label / len(uniquelabels))
    plt.scatter(datapca[labels == label, 0], datapca[labels == label, 1], c=color, label=f'Cluster {label}')

plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('DBSCAN Clustering with PCA')
plt.legend()
plt.show()
