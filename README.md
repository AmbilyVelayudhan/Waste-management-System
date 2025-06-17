# Waste-management-System

♻️ AI-Powered Waste Management System

A Streamlit web app that classifies waste types from images using a Convolutional Neural Network (CNN) and provides eco-friendly disposal tips.


📌 Project Objective

  The goal of this project is to develop an AI-based waste management system that:

* Automatically classifies types of waste (plastic, paper, glass, etc.) using image inputs.

* Educates users by offering disposal suggestions for each category.

* Encourages proper recycling and waste segregation to promote environmental sustainability.
  

📂 Dataset Used
  
 The dataset is a labeled image collection consisting of six categories of waste:

  - cardboard
   
  - glass

  - metal

  - paper

  - plastic

  - trash
    

⚙️ Features
    
✅ Upload a waste image and get real-time predictions
✅ Trained deep learning model (CNN) for classification
✅ Streamlit-powered intuitive interface
✅ Smart disposal tips for sustainable living
✅ Lightweight and portable (runs locally)

🛠️ Tech Stack

- Python

- TensorFlow / Keras (for model training)

- Streamlit (for frontend UI)

- Pillow, NumPy (image preprocessing)
  

🚀 Project Structure

waste_management_system/
│
├── app.py                    
├── train_model.py             
├── utils.py                   
├── model/
│   └── waste_classifier.h5    
├── dataset/
│   └── TrashType_Image_Dataset/  
├── temp/                     
├── requirements.txt         
└── README.md           

🧪 How It Works

1. User uploads an image of a waste item.

2. The image is preprocessed and passed to the CNN model.

3. The model predicts the waste type with a confidence score.

4. Based on the result, disposal suggestions are shown.

   
💻 Installation & Running the App

1. Clone the repository

git clone https://github.com/your-username/waste-management-system.git
cd waste-management-system

2. Install the dependencies

pip install -r requirements.txt

3. Train the model (if not already trained)

python train_model.py

4. Launch the app

streamlit run app.py






