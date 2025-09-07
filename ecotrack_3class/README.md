# EcoTrack – AI Waste Classifier

This is a simple Streamlit web app that classifies waste images into 3 categories: **Organic, Recyclable, Hazardous**.

## Files
- `app.py` – Streamlit app code
- `requirements.txt` – Required Python libraries
- `waste_model_3class.h5` – Pre-trained Keras model (3-class)

## Run Instructions
1. Place `waste_model_3class.h5` in the project folder.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   streamlit run app.py
   ```
