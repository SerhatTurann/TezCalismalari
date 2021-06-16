import cv2 #Görüntü işleme kütüphanesi.
import numpy as np #matris işlemleri için kullanılır.

#Kendi yazdığımız sınıflar dahil edilir.
import GarbageResNet as resnet
import Servo as servo

image = cv2.imread("image_deneme/kagit.jpg")#Belirtilen yoldaki dosya okunur.

image_resnet,label = resnet.TahminEt(image)#Okunan görüntü modelde tahmin edilir.
#Sonuç görüntü üzerine işlenerek döndürülür.
cv2.imshow('Cop Siniflandirmasi', image_resnet)#Sonuç ekrana bastırılır.

print('etiket : ',label)#Tahminden dönen etiket değeri ekrana yazılır.
servo.cope_tasi(label)#Etiket değeri servo sınıfındaki çöpe taşı fonksiyonuna verilir.
#Çöpe taşı fonksiyonu aldığı etiketi uygun çöpe atma işlemini sağlar.

cv2.waitKey(0)#Bekleme komutu.
cv2.destroyAllWindows()#Tüm pencereleri kapatma komutu.
