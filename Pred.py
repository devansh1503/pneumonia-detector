import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from PIL import Image
import os
model = tf.keras.models.load_model('chest_xray_cnn')
def predict():
    ds_eval = tf.keras.preprocessing.image_dataset_from_directory(
        './inputimg',
        labels="inferred",
        label_mode="int", 
        color_mode="rgb",
        image_size=(64, 64),
    )
    res = model.predict(ds_eval)
    if (res[0][0]>0.5):
        return 'Pneumonia Detected'
    else:
        return 'Normal'