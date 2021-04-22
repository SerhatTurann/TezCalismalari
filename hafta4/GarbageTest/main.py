import cv2 #Görüntü işleme kütüphanesi.
import numpy as np #matris işlemleri için kullanılır.
import glob #dosya işlemleri için kullanılır.

#Kendi yazdığımız modüller dahil edilir.
import GarbageInception as inception
import GarbageCNN as cnn
import GarbageVGG as vgg
import GarbageResNet as resnet

for fname in glob.glob('test_images_garbage\*.jpg'):
    #glob komutuyla ilgili test doyasındaki jpg uzantılı görüntüler okunur.
    #for döngüsü dosyadaki görüntüler bitene kadar devam eder.
    image = cv2.imread(fname)#görüntü anlık okunur.
    #Kendi oluşturduğumuz modüllere sırası ile resimler yollanır
    # ve tahmin sonuçları alınır.
    image_inception = inception.TahminEt(image)
    image_cnn = cnn.TahminEt(image)
    image_resnet = resnet.TahminEt(image)
    image_vgg = vgg.TahminEt(image)

    #Görüntünün 2x2 lik bir tablo gibi birleştirilmesi sağlanır.
    yatay1 = np.hstack((image_inception, image_cnn))
    yatay2 = np.hstack((image_resnet, image_vgg))
    dikey = np.vstack((yatay1, yatay2))

    #Görüntünün son hali ekrana bastırılır.
    cv2.imshow('Cop Siniflandirmasi', dikey)
    cv2.waitKey(0)
cv2.destroyAllWindows()