import pickle


# Load the trained model and vectorizer
filename = 'categories_classification_model.pkl'
with open(filename, 'rb') as file:
    clf, vectorizer = pickle.load(file)

# Ask the user to input the text to be classified
input_text = input("Vui lòng nhập văn bản cần phân tích: ")

# Vectorize the input text
X_input = [input_text]
X_input_vectorized = vectorizer.transform(X_input)

# Make the prediction
prediction = clf.predict(X_input_vectorized)

# Print the result
print("Nhãn dự đoán: ",prediction[0])