from flask import Flask, request, jsonify, render_template
import numpy as np
import pickle
import tensorflow as tf
from tensorflow.keras.preprocessing.image import img_to_array, load_img
from werkzeug.utils import secure_filename
import os

# Initialize the Flask application
app = Flask(__name__)

# Load the fine-tuned models from the pickle file
with open('fine_tuned_models.pkl', 'rb') as f:
    loaded_models = pickle.load(f)


# Function to create ensemble predictions
def create_ensemble(models, image_array):
    preds = [model.predict(image_array) for model in models]
    avg_preds = np.mean(preds, axis=0)
    return avg_preds


# Define the route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Define the route to handle image uploads and predictions
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'})

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No file selected'})

    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join('uploads', filename)
        file.save(file_path)

        # Load and preprocess the image
        image = load_img(file_path, target_size=(224, 224))  # Assuming the models expect 224x224 images
        image_array = img_to_array(image) / 255.0
        image_array = np.expand_dims(image_array, axis=0)  # Add batch dimension

        # Create ensemble predictions
        model_names = ['VGG16', 'InceptionV3', 'EfficientNetB0']
        ensemble_models = [loaded_models[name] for name in model_names]
        ensemble_predictions = create_ensemble(ensemble_models, image_array)

        # Get the final class prediction
        predicted_class_idx = np.argmax(ensemble_predictions, axis=1)[0]
        predicted_class_prob = np.max(ensemble_predictions, axis=1)[0]

        # Define a threshold below which the model is not confident
        confidence_threshold = 0.6

        if predicted_class_prob < confidence_threshold:
            result = "Unfortunately, model cannot predict with confidence. Please consult your doctor for further analysis."
        else:
            class_labels = ['glioma', 'meningioma', 'notumor', 'pituitary']  # Update according to your class names
            predicted_class = class_labels[predicted_class_idx]
            result = f"Predicted class: {predicted_class} with confidence {predicted_class_prob:.2f}"

        # Render the result in the template
        return render_template('result.html', result=result)


if __name__ == '__main__':
    app.run(debug=False)
