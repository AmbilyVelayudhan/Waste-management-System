import streamlit as st
from utils import predict_waste
import os

TEMP_DIR = "temp"
os.makedirs(TEMP_DIR, exist_ok=True)

st.title("♻️ AI-Powered Waste Classification System")
st.write("Upload an image of waste, and the AI will classify it!")

uploaded_file = st.file_uploader("Upload a waste image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
   
    file_path = os.path.join(TEMP_DIR, uploaded_file.name)

   
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

   
    st.image(file_path, caption="Uploaded Image", use_column_width=True)

   
    label, confidence = predict_waste(file_path)
    st.success(f"Predicted Waste Category: **{label.capitalize()}** ({confidence:.2f} confidence)")

    
    disposal_tips = {
        "cardboard": "Recycle in paper bins or reuse if possible.",
        "glass": "Dispose in glass recycling bins. Handle broken glass with care.",
        "metal": "Recycle metal in designated bins. Avoid contamination.",
        "paper": "Recycle clean paper. Avoid mixing with food waste.",
        "plastic": "Recycle plastics based on their type (check recycling codes).",
        "trash": "Dispose in general waste bins. Reduce landfill waste!"
    }
    st.info(f"**Disposal Tip:** {disposal_tips[label]}")

   
    os.remove(file_path)
