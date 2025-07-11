import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
data={
    'sqrfeet':[1400,1200,1600,1800,1100],
    'rooms':[3,2,4,5,1],
    'age':[10,5,15,7,20],
    'price':[75,65,80,90,60],
}
df=pd.DataFrame(data)
x = df[['sqrfeet', 'rooms', 'age']]
y = df['price']
#x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
model = DecisionTreeRegressor()
model.fit(x, y)
new_house=[[1600,5,2]]
predicton_price=model.predict(new_house)
print(predicton_price[0])


