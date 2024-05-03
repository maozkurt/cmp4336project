from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt
import pandas as pd

# read dataset from csv
dataset = pd.read_csv('./dataset.csv')

# drop address column 
X = dataset.drop(columns=['Address']).values

# hierarchical clustering
Z = linkage(X, method='ward')  

# plotting
plt.figure(figsize=(12, 6))
plt.title('Hierarchical Clustering')
plt.xlabel('Addresses')
plt.ylabel('Distance')
dendrogram(
    Z,
    leaf_rotation=90.,  
    leaf_font_size=8.,  
    labels=dataset['Address'].values  
)
plt.show()
