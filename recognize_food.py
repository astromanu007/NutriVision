import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

# Load the trained model
model = load_model('food_recognition_model.h5')

# Function to preprocess input image
def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    return img_array / 255.

# Function to predict food item and estimate calorie content
def predict_calories(img_path):
    img_array = preprocess_image(img_path)
    predictions = model.predict(img_array)
    predicted_class = np.argmax(predictions)
    return predicted_class, predictions[0][predicted_class]

# Example usage
image_path = 'path/to/your/image.jpg'
food_class, confidence = predict_calories(image_path)
print(f'Predicted Food Class: {food_class}, Confidence: {confidence}')
