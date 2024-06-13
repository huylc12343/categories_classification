import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load the dataset
data = pd.read_csv('data.csv')

# Extract the text and labels
X = data['text']
y = data['label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


vectorizer = CountVectorizer()
X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)


clf = MultinomialNB()
clf.fit(X_train_vectorized, y_train)

# Evaluate the model on the test set
y_pred = clf.predict(X_test_vectorized)
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')

import pickle

# Lưu model
# Save the model and vectorizer
filename = 'categories_classification_model.pkl'
with open(filename, 'wb') as file:
    pickle.dump((clf, vectorizer), file)
