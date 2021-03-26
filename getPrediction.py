import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
from keras.preprocessing import image
model = load_model('models/asl_model_5.h5')

def get_prediction(filename):
    path = 'static/'+filename
    img = image.load_img(path, target_size=(200,200))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)

    images = np.vstack([x])
    classes = model.predict(images, batch_size=1)
    prediction='idk'


    for i in range (65, 91):
        if classes[0][i-65]==1:
            prediction=chr(i)
    if classes[0][26]==1:
        prediction='delete'
    elif classes[0][27]==1:
        prediction='space'
    elif classes[0][28]==1:
        prediction='nothing'

    return(prediction)


    
