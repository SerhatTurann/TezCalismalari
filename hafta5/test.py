import cv2 #Görüntü işleme kütüphanesi.
import numpy as np #matris işlemleri için kullanılır.

#Kendi yazdığımız modüldahil edilir.
import GarbageInception as inception

image = cv2.imread("images/gorsel.jpg")#Belirtilen yoldaki dosya okunur.

image_inception,_ = inception.TahminEt(image)#Okunan görüntü modelde tahmin edilir.
#Sonuç görüntü üzerine işlenerek döndürülür.
cv2.imshow('Cop Siniflandirmasi', image_inception)#Sonuç ekrana bastırılır.
cv2.waitKey(0)#Bekleme komutu.
cv2.destroyAllWindows()#Tüm pencereleri kapatma komutu.
