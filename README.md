# Brain Tumor Classification Flask Application.

## Overview

This project is a web application built using Flask that allows users to upload brain MRI images and receive predictions about the presence of specific brain tumors. The application uses an ensemble of fine-tuned deep learning models (VGG16, InceptionV3, and EfficientNetB0) to predict the type of tumor. If the model is uncertain about the prediction, the user is advised to consult a doctor.

## Features

- **Image Upload**: Users can upload brain MRI images in JPG, PNG, or JPEG format.
- **Ensemble Model Prediction**: The app uses an ensemble of deep learning models to predict the tumor type with increased accuracy.
- **Confidence Threshold**: If the model is not confident in its prediction, it suggests consulting a doctor.
- **Responsive UI**: A user-friendly and responsive interface with real-time image preview.
- **Model Interpretability**: Integrates SHAP for model interpretability.

## Technologies Used

- **Backend**: Python, Flask, TensorFlow, Keras, NumPy, SHAP
- **Frontend**: HTML, CSS, JavaScript (with Bootstrap 5)
- **Model Persistence**: Pickle
- **Deployment**: Gunicorn (optional for production)

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.8+
- TensorFlow
- Flask
- Keras
- SHAP
- Bootstrap 5 (included via CDN in `index.html`)

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/disisvm/ScanSmart-AI.git
   cd brain-tumor-classification-app
   ```

2. **Install the dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Prepare the models**:

   Firstly execute the `scansmart-ai.ipynb` file to generate the pickle file. Ensure that the `fine_tuned_models.pkl` file is placed in the root directory of the project. This file contains the pre-trained models.

4. **Run the application**:

   ```bash
   python app.py
   ```

5. **Open the application**:

   Open your web browser and navigate to `http://127.0.0.1:5000/`.

### Usage

- Upload a brain MRI image.
- The application will process the image and return a prediction about the tumor type.
- If the model is not confident, it will suggest consulting a doctor.

## Project Structure

```
.
├── app.py               # Main Flask application
├── static/
│   ├── css/
│   │   └── styles.css   # Custom CSS styles
│   ├── js/
│   │   └── scripts.js   # JavaScript file for UI interactions
├── templates/
│   └── index.html       # HTML template for the main page
├── uploads/             # Directory for uploaded images (created at runtime)
├── fine_tuned_models.pkl  # Serialized model file (not included in the repo)
├── scansmart-ai.ipynb   # Model training and evaluation
├── requirements.txt     # Python dependencies
└── README.md            # This README file
```


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- The fine-tuned models used in this project are based on popular architectures available in Keras.
- Special thanks to the [Kaggle dataset](https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset) used for training the models.
