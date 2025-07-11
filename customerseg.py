import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
data={
    'customerId':[1,2,3,4,5,6,7,8,9,10],
    'AnnualIncome':[15,16,17,60,62,63,90,91,92,93],
    'SpendAmount':[39,81,6,77,40,5,88,20,10,96]

}
df=pd.DataFrame(data)
x=df[['AnnualIncome','SpendAmount']]
kmeans=KMeans(n_clusters=3,random_state=42)
df['cluster']=kmeans.fit_predict(x)
print(df)
plt.figure(figsize=(8,6))
plt.scatter(df['AnnualIncome'],df['SpendAmount']
            ,c=df['cluster'],s=100)
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],c="red",marker="x", s=200, label='Centroids')
plt.legend()
plt.grid(True)
plt.show()