import pandas as pd
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
df=pd.read_csv("Amazon Sale Report.cvs")
print(df.head(5))
#order ID qty amount
segmentation_df=df[['Order ID',]]
