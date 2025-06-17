import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image


MODEL_PATH = "model/waste_classifier.h5"
model = tf.keras.models.load_model(MODEL_PATH)


CLASS_LABELS = ['cardboard', 'glass', 'metal', 'paper', 'plastic', 'trash']

def predict_waste(img_path):
    """Predicts the waste category from the image."""
    img = image.load_img(img_path, target_size=(150, 150))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0

    predictions = model.predict(img_array)
    class_index = np.argmax(predictions)
    return CLASS_LABELS[class_index], predictions[0][class_index]
