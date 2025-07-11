import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
df=pd.read_csv("Housing.csv")
#print(df.columns)
x=df[['area','bedroom','guestroom']]
df['price']=df['price'].astype(float)
y=df['price']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
model=DecisionTreeRegressor()
model.fit(x_train,y_train)
new_house=[[3750,4]]
prediction=model.predict(new_house)
print(prediction[0])


