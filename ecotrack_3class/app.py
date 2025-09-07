import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Load model
model = tf.keras.models.load_model("waste_model_3class.h5")

# Class labels (3-class model)
class_names = ['Organic', 'Recyclable', 'Hazardous']

st.title("♻️ EcoTrack – AI Waste Classifier")
st.write("Upload a waste image and get instant classification!")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg","jpeg","png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Preprocess
    img = image.resize((128,128))
    img_array = np.array(img)/255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Prediction
    predictions = model.predict(img_array)
    class_idx = np.argmax(predictions)
    confidence = round(100 * np.max(predictions), 2)

    st.success(f"Prediction: **{class_names[class_idx]}** ({confidence}% confidence)")