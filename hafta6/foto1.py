import cv2 #Görüntü işleme kütüphanesi.
import numpy as np #matris işlemleri için kullanılır.
import glob #dosya işlemleri için kullanılır.
#import tensorflow as tf 
import picamera#Kamera modülünün Python arayüzünde kullanımını sağlayan kütüphanedir.

cam = picamera.PiCamera()# PiCamera içerisinde bulunan fonksiyonlarının
#kullanımı için bir cam nesnesi tanımlanır.

#fotograf_cek fonksiyonu bir fotoğraf çeker bunu images klasörüne kaydeder.
def fotograf_cek():
    file_name = "images/gorsel.jpg"#Dosya yolu
    cam.capture(file_name)#Anlık görüntü yakalar.(Fotoğraf çeker.)
    print("Fotoğraf çekildi.")
        
fotograf_cek()