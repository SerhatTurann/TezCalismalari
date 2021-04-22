import cv2 #Görüntü işleme kütüphanesi.
import numpy as np #matris işlemleri için kullanılır.
import Tools #Label işlemleri için kendi yazdığımız modül
#Modeli yüklemek ve giriş görüntüsünü hazırlamak için gerekli kütüphaneler.
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications.resnet50 import preprocess_input

#Model yüklenir ve etiket işlemleri yapılır.
model = load_model('models\model_resnet50_10-0.82.h5')
labels, lb = Tools.labels()

def TahminEt(image):
    #Gelen görüntü okunur ve modelin girişine hazırlanır.
    output = image.copy()
    image = cv2.resize(image,(224,224))
    image = preprocess_input(image)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    #Hazırlanan görüntü modele verilir ve tahmin sonucu alınır.
    #Etiketleri Türkçeye çevirilir, yüzdelik değerleri hesaplanır.
    proba = model.predict(image)[0]
    idx = np.argmax(proba)
    label = lb.classes_[idx]
    label = Tools.cevir(label)
    label = "{}: {:.2f}% ".format(label, proba[idx] * 100)
    output = cv2.putText(output, label+'-'+'ResNet', (10, 25), cv2.FONT_HERSHEY_SIMPLEX,
                0.7, (0, 0, 255), 2)
    output = cv2.resize(output, (300, 300))#Görüntü üzerine bu bilgiler yazılır.
    return output #Görüntü döndürülür.