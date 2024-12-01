import logging
import os
import warnings

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
logging.getLogger("tensorflow").setLevel(logging.ERROR)
warnings.filterwarnings("ignore")  # WARNING HATAO PRAN BACHAO

import absl.logging
absl.logging.set_verbosity(absl.logging.ERROR)
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array

model = load_model("waste_classifier.h5")

test_image_path = "img.jpg"

img = load_img(test_image_path, target_size=(150, 150))
img_array = img_to_array(img) / 255.0  
img_array = np.expand_dims(img_array, axis=0) 

prediction = model.predict(img_array)[0][0]

category = "Biodegradable" if prediction < 0.5 else "Non-Biodegradable"
confidence = 1 - prediction if category == "Biodegradable" else prediction
confidence *= 100
print(f"The image is classified as: {category} with confidence: {confidence:.2f}%")
