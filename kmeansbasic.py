import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
#dataset creation
data=np.array([[1,2],[1.5,1.8],[5,8],[8,8],[5,10],[1,0.6],[9,11]])
#Creation model
kmeans=KMeans(n_clusters=3,random_state=42)
kmeans.fit(data)
#get predictions(Cluster and labels)
labels=kmeans.predict(data)
centers=kmeans.cluster_centers_
#visualize
colors=["red","green","orange"]
for i in range(len(data)):
    plt.scatter(data[i][0],data[i][1],c=colors[labels[i]],label=f"point{i}")
plt.scatter(centers[:,0],centers[:,1],c="blue",marker='x',s=200,label='centeriods')
plt.title("K-means clustering")
plt.legend()
plt.grid(True)
plt.show()