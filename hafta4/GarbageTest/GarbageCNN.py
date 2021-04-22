from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
import cv2
import numpy as np
import Tools
model = load_model('models\garbage_cnn.h5')

labels, lb = Tools.labels()

def TahminEt(image):
    output = image.copy()
    image = cv2.resize(image, (300, 300))
    image = image.astype("float") / 255.0
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    # make bounding box predictions on the input image
    proba = model.predict(image)[0]
    idx = np.argmax(proba)
    label = lb.classes_[idx]
    label = Tools.cevir(label)
    label = "{}: {:.2f}% ".format(label, proba[idx] * 100)
    output = cv2.putText(output, label+'-'+'CNN', (20, 25), cv2.FONT_HERSHEY_SIMPLEX,
                0.7, (0, 0, 255), 2)
    output = cv2.resize(output,(300,300))
    return output