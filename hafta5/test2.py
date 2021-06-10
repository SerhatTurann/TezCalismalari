import cv2 #Görüntü işleme kütüphanesi.
import numpy as np #matris işlemleri için kullanılır.
import glob #Dosya işlemleri için kullanılır.
import GarbageInception as inception#Kendi yazdığımız modül dahil edilir.

## Tahminler fonksiyonu images klasöründe bulunan fotoğrafları teker teker tahmin ettirir
# ve tahmin sonuçlarını bir dizi olarak geri döndürür.
def tahminler():
    label_list = [] #Boş bir label listesi tanımlanmıştır.
    for fname in glob.glob('images/*.jpg'):#Klasördeki dosyalarda gezilir.
        image = cv2.imread(fname)#görüntü anlık okunur
        _, label = inception.TahminEt(image)#Görüntülerin tahmin sonuçları alınır.
        label_list.append(label)#Tahmin sonuçları listeye eklenir.
    return label_list #Liste döndürülür.

##Saydır fonksiyonu parametre olarak bir liste ve ifade alır.
#Bu ifadenin listede ne kadar tekrarlandığının bilgisini geri döndürür.
def saydir(lst, eleman):
    adet = 0
    for elem in lst:
        if(elem == eleman):
            adet = adet+1
    return adet

#Hesapla fonksiyonu içerisine bir liste alır. Bu listede modelden dönen tahmin sonuçları bulunmaktadır.
#Dönen tahmin sonuçlarının hangi kategoriye ait oldukları ve kaç kere tekrarlandığının bilgisi
#saydır fonksiyonu ile alınır ve bir sözlükte tutulur.
#En çok kullanılan elemanı geri döndürür. Bu şekilde modelin tahmin sonucunun doğruluğunu arttırmak amaçlanmıştır.
def hesapla(liste):
    karton_sayisi = saydir(liste, 'KARTON')
    kagit_sayisi = saydir(liste, 'KAGIT')
    plastik_sayisi = saydir(liste, 'PLASTIK')
    cam_sayisi = saydir(liste, 'CAM')
    metal_sayisi = saydir(liste, 'METAL')
    trash_sayisi = saydir(liste, 'TRASH')
    sozluk = {'KARTON' :karton_sayisi, 'CAM' :cam_sayisi, 'KAGIT' :kagit_sayisi,
              'PLASTIK' :plastik_sayisi, 'METAL' :metal_sayisi, 'TRASH' :trash_sayisi}    
    max_eleman = max(sozluk, key = sozluk.get)#En büyük eleman hesaplanır.
    return max_eleman

liste = tahminler() #Tahmin sonuçları bir listede tutulur.
max_ele = hesapla(liste)#Tahmin sonucunda en çok tahmin edilen kategori bulunur.
print(max_ele)#En çok tekrarlanan kategori ekrana yazdırılır. 
