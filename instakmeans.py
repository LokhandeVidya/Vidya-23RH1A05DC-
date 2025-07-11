from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
import matplotlib.pyplot as plt


from sklearn.decomposition  import PCA
import numpy as np
import pandas as pd
hashtags=[
"Morning Workout #gym #fitness",
"Delicious choclate cake receipe #foodie #dessert",
"Leg day at the gym! #fitness #workout",
"traveling to the Mountains #travel #nature",
"choclate lava cake is my weakness #foodie #choclate",
"Exploring a beatiful waterfall #nature #travel",
"deadlifts and squats today #gym #fitness",
"Easy pasta recipe for dinner #foodie #cooking",
"sunrise hike wasworth it ! #hiking #mountain #nature",
"meal prep ideas for the fat loss #fitness #food #mealprep"]
#clean dataset and convert hashtag into Matrix
vectorizer=TfidfVectorizer(stop_words='english')
x=vectorizer.fit_transform(hashtags)
# food nature fitness
kmeans=KMeans(n_clusters=3,random_state=42)
kmeans.fit(x)
labels=kmeans.labels_
#convert to Data frame and show resuult
cluster_names_map={0:"nature",1:"foodie",2:"gym"}
df=pd.DataFrame({'caption':hashtags,'cluster':labels})
df['category']=df['cluster'].map(cluster_names_map)
print(df.sort_values('cluster'))


#plotting
#visival using PCA
x_array=x.toarray()
pca=PCA()
x_reduced=pca.fit_transform(x_array)
#plotting
plt.figure(figsize=(8,5))
scatter=plt.scatter(x_reduced[:,0],x_reduced[:,1],
     c=labels,s=100)
for i,row in df.iterrows():
    plt.annotate(row['category'],(x_reduced[i,0]+00.5,x_reduced[i,1]+0.05),fontsize=8)
plt.show()






