import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

#------------------------

refcount = pd.read_csv('Unique/refcountfromscrape.csv')
cunewness = pd.read_csv('Unique/CU_trendypaperpercentage_update.csv')

merge_df = pd.merge(refcount, cunewness, on='filename', how='inner')

print("Merged Data preview:")
print(merge_df.head())

features = merge_df[['refcount', 'global']].to_numpy()

#------------------------

k = 2

kmeans = KMeans(n_clusters=k, n_init=30, random_state=42)
kmeans.fit(features)

cluster_centers = kmeans.cluster_centers_
labels = kmeans.labels_

#---------------------

merge_df['cluster'] = labels

merge_df[['filename', 'refcount', 'global', 'cluster']].to_csv('kMeansResult/cu_kmeans_newness.csv', index=False)

print("New file 'cu_kmeans_newness.csv' created.")

#---------------------

plt.figure(figsize=(10, 8)) 
for i in range(k):
    cluster_points = features[labels == i]
    plt.scatter(cluster_points[:, 0], cluster_points[:, 1], label=f"Cluster {i}")

plt.scatter(cluster_centers[:, 0], cluster_centers[:, 1], s=200, c='red', marker='X', label='Centroids')

plt.title("CU newness-refcount")
plt.xlabel("ref-count")
plt.ylabel("percentage of newness(%)")
plt.legend()
plt.grid(True)

plt.show()
