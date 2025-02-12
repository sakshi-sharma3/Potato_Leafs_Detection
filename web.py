import streamlit as st
import tensorflow as tf
import numpy as np
def model_prediction(test_image):
    model = tf.keras.models.load_model("trained_plant_disease_model.keras")
    image = tf.keras.preprocessing.image.load_img(test_image,target_size=(128,128))
    input_arr =tf.keras.preprocessing.image.img_to_array(image)
    input_arr=np.array([input_arr])
    predictions =model.predict(input_arr)
    return np.argmax(predictions)
st.sidebar.title("Plant Disease system for Sustainable Agriculture")
app_mode = st.sidebar.selectbox("Select page",['Home','Disease Recognition'])

from PIL import Image

img = Image.open("disease prediction.jpg")
st.image(img)

if(app_mode=='HOME'):
    st.markdown("<h1 style='text_align: center;'>Plant Disease Detection System for sustainable Agriculture",unsafe_allow_html=True)

elif(app_mode=="Disease recognition"):
    st.header("Plant Disease Detection System for sustainable Agriculture")

test_image=st.file_uploader('choose an image:')
if(st.button('Show Image')):
    st.image(test_image,width=4,use_column_width=True)

if(st.button("Predict")):
    st.snow()
    st.write("our predictions")
    result_index = model_prediction(test_image)
    class_name=['Potato__Early_blight','Potato__Late_blight','Potato__healthy']
    st.success('Model is predicting its a {}'.format(class_name[result_index]))
