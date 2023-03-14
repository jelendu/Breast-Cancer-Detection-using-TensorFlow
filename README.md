import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split

# Load the dataset
dataset = pd.read_csv('cancer.csv')

# Split the dataset into input (x) and output (y) variables
x = dataset.drop(columns=['diagnosis(1=m, 0=b)'])
y = dataset['diagnosis(1=m, 0=b)']

# Split the dataset into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# Define the model architecture
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(256, input_shape=(30,), activation='sigmoid'),
    tf.keras.layers.Dense(256, activation='sigmoid'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(x_train, y_train, epochs=1000)

# Evaluate the model on the testing data
loss, accuracy = model.evaluate(x_test, y_test)
print(f'Test Loss: {loss:.4f}')
print(f'Test Accuracy: {accuracy:.4f}')
