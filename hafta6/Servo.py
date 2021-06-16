import serial#Seri port işlemleri için kullanılır.
import time#Zaman  fonksiyonlarını içinde barındırır. 
ser = serial.Serial('/dev/ttyUSB0',9600)#Ardunio raspberrye direk usb kablosu ile bağlanmıştır.
#Bu sebebten dolayı ardunionun raspberrydeki bulunduğu konum ve verilen isim,
#haberleşme için değişkende tutulur.  

#Buradaki fonksiyonlar etiket durumlarına göre belirlenen değerleri seri port ekranına yazar.
#Seri port ekranından veriler ardunioya aktarılır. Ardunio tarafından servo motor kontrol edilir.
#Bu şekilde çöpe taşıma işlemi sağlanır.
def karton_veya_kagit():
    ser.write('A'.encode('utf-8'))#Seri port ekranına değer yazılır.
    time.sleep(5)#Bekleme komutu
    
def plastik():
    ser.write('B'.encode('utf-8'))#Seri port ekranına değer yazılır.
    time.sleep(5)#Bekleme komutu

def cam():
    ser.write('C'.encode('utf-8'))#Seri port ekranına değer yazılır.
    time.sleep(5)#Bekleme komutu

def metal():
    ser.write('D'.encode('utf-8'))#Seri port ekranına değer yazılır.
    time.sleep(5)#Bekleme komutu

#Tahminden gelecek etiket değeri bu fonksiyona giriş değeri olarak verilir.
#Etiket değerine göre uygun fonksiyon çağrılarak çöpe taşıma işlemi sağlanır. 
def cope_tasi(label):
    if(label == 'KARTON' or label == 'KAGIT'):
        karton_veya_kagit()
    elif(label == 'PLASTIK'):
        plastik()
    elif(label == 'CAM'):
        cam()
    elif(label == 'METAL'):
        metal()
    print('Nesne çöpe taşındı.')
        