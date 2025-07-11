import tensorflow as tf
import numpy as np
x = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 0, 0, 1]) 
#create model
model = tf.keras.Sequential([tf.keras.layers.Dense(units=1, input_shape=(2,), activation='sigmoid')])
#create model
model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])
#train model
model.fit(x,y,epochs=100,verbose=0)
#evaluate
loss,accuracy=model.evaluate(x,y,verbose=0)
print(f"Accuracy:",accuracy)
#predict
predictions=model.predict(x)
for i in range(len(x)):
  print(f"{x[i]}->{predictions[i][0]}->{int(predictions[i][0]>0.5)}")