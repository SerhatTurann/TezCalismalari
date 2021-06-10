import cv2 #Görüntü işleme kütüphanesi.
import numpy as np #matris işlemleri için kullanılır.
import glob #dosya işlemleri için kullanılır.

import picamera #Kamera modülünün Python arayüzünde kullanımını sağlayan kütüphanedir.
from time import sleep #Zamanlama işlemleri için kullanılır.
#Sleep bekletmek için kullanılır.

cam = picamera.PiCamera()# PiCamera içerisinde bulunan fonksiyonlarının
#kullanımı için bir cam nesnesi tanımlanır.

#Fotoğraf çek fonksiyonu iki saniye arayla üç adet fotoğraf çeker ve images klasörüne kaydeder.
def fotograf_cek():
    for i in range(3):
        file_name = "images/gorsel{f}.jpg".format(f = i)#Dosya yolu
        cam.capture(file_name)#Anlık görüntü yakalar.(Fotoğraf çeker.)
        print("Fotoğraf çekildi.")
        sleep(2)#İki saniye bekler.
        
fotograf_cek()


