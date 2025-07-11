import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import CountVectorizer

data={
    'messages':['with a free lottery ticket',' hi, find ur attachement file	','kudos, you won a car','meet you at 10am tomorrow','claim your free gift','Terrorist planned bomb blast in mrecw','you won lottery price'],
    'status':['spam','not spam', 'spam','not spam','spam','spam','spam'],
}
df=pd.DataFrame(data)
df['status'] = df['status'].map({'spam': 1, 'not spam': 0})

x = df['messages']
y = df['status']
vectorizer=CountVectorizer()
x_vectorizer=vectorizer.fit_transform(x)#converts into text and store as a number
x_train, x_test, y_train, y_test = train_test_split(x_vectorizer, y, test_size=0.3,random_state=42)
model = LogisticRegression()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
sample_message=["free prize waiting for u"]
sample_vector=vectorizer.transform(sample_message)
prediction=model.predict(sample_vector)
print(prediction[0])


