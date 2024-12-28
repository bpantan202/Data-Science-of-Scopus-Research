import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

#------------------------

refcount = pd.read_csv('Book/KU_cited.csv')
kuglobal = pd.read_csv('Unique/KU_globalpercentage_update.csv')

merge_df = pd.merge(refcount, kuglobal, left_on='order', right_on='order')

print("Merged Data preview:")
print(merge_df.head())

features = merge_df[['cited_count', 'global']].to_numpy()

# #------------------------

k = 2

kmeans = KMeans(n_clusters=k, n_init=30, random_state=42)
kmeans.fit(features)

cluster_centers = kmeans.cluster_centers_
labels = kmeans.labels_

#---------------------

merge_df['cluster'] = labels

merge_df[['order', 'cited_count', 'global', 'cluster']].to_csv('kMeansResult/ku_kmeans_global.csv', index=False)

print("New file 'ku_kmeans_global.csv' created.")

#---------------------

plt.figure(figsize=(10, 8)) 
for i in range(k):
    cluster_points = features[labels == i]
    plt.scatter(cluster_points[:, 0], cluster_points[:, 1], label=f"Cluster {i}")

plt.scatter(cluster_centers[:, 0], cluster_centers[:, 1], s=200, c='red', marker='X', label='Centroids')

plt.title("KU global - cited-count")
plt.xlabel("cited-count")
plt.ylabel("percentage of global(%)")
plt.legend()
plt.grid(True)

plt.show()