import streamlit as st
import tensorflow as tf
import numpy as np
import gdown
import os
file_id ='1Jzcz4qaqf761871cH1aNGEpWW8zX6JY0'
url='https://drive.google.com/file/d/1Jzcz4qaqf761871cH1aNGEpWW8zX6JY0/'
model_path ="trained_plant_disease_model.keras"

if not os.path.exists(model_path):
    st.warning("Downloading model from Google Drive..")
    gdown.download(url,model_path,quiet=False)


    
def model_prediction(test_image):
    model = tf.keras.models.load_model("trained_plant_disease_model.keras")
    image = tf.keras.preprocessing.image.load_img(test_image,target_size=(128,128))
    input_arr =tf.keras.preprocessing.image.img_to_array(image)
    input_arr=np.array([input_arr])
    predictions =model.predict(input_arr)
    return np.argmax(predictions)