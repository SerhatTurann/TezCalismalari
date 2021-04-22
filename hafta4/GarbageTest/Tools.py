import numpy as np #matris işlemleri için kullanılır.
from sklearn.preprocessing import LabelBinarizer
#etiketleri binarize etmek için kullanılan kütüphanedir.

#Labellar binarize edilir ve sonuç döndürülür.
def labels():
    LABELS = ["CARDBOARD", "GLASS", "METAL", "PAPER", "PLASTIC", "TRASH"]
    labels = np.array(LABELS)
    lb = LabelBinarizer()
    labels = lb.fit_transform(labels)

    return labels,lb

#Etiketler Türkçeye çevirilir.
def cevir(label):
    if (label == 'CARDBOARD'):
        label = 'KARTON'
    elif (label == 'GLASS'):
        label = 'CAM'
    elif (label == 'PAPER'):
        label = 'KAGIT'
    elif (label == 'PLASTIC'):
        label = 'PLASTIK'

    return label

