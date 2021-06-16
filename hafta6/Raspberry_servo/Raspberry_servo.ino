#include<Servo.h>//Servo kütüphanesi sisteme dahil edilir.

Servo motor;
int from_pi = 0; //Serial porttan gelecek değeri tutmak için bir nesne oluşturuldu.

void setup() {
  Serial.begin(9600); //Serial Port başlatıldı ve 9600 hızı verildi.
  motor.attach(3);
}

void loop() {
 Serial.println("ARDUİNO AKTİF");//Seri porta arduino'nun aktif olduğu bilgisi sunuldu.
 delay(1000);//Bir saniye bekler.
 if(Serial.available()>0)//Serial Porta girdi değerinin olup olmadığı kontrol edilir. 
 {
  from_pi = Serial.read();//Seri porttaki değer okunur ve "from_pi" değişkenine atanır.
  Serial.print("Alinan Deger: ");
  Serial.print(from_pi);
  Serial.print(" - Char Olarak Alinan Deger: ");
  Serial.println((char)from_pi);//Alınan değer chara dönüştürülür ve seri porta yazılır.

  //Raspberryden char şeklinde veriler gelir. Alınan değerler sırasıyle iflerle kontrol edilir.
  //Her harf bir etikete gelecek şekilde ayarlanmıştır.
  //A : Karton veya kağıt, B : Plastik, C : Cam, D : Metal
  if(from_pi == 'A')//Karton veya kağıt olma olasılığında yapılacaklar.
  {
      motor.write(0); //Servo motor açı değeri olarak 0 dereceye döndürülür.
      delay(2000);//İki saniye beklenir.
      from_pi = 0;// "from_pi" değişkenine ilk değeri atanır.
  }

  if(from_pi == 'B')//Plastik olma olasılığında yapılacaklar.
  {
      motor.write(60); //Servo motor açı değeri olarak 60 dereceye döndürülür.
      delay(2000);//İki saniye beklenir.
      from_pi = 0;
  }
  if(from_pi == 'C')//Cam olma olasılığında yapılacaklar.
  {
      motor.write(120); //Servo motor açı değeri olarak 120 dereceye döndürülür.
      delay(2000);//İki saniye beklenir.
      from_pi = 0;// "from_pi" değişkenine ilk değeri atanır.
  }
  if(from_pi == 'D')//Metal olma olasılığında yapılacaklar.
  {
      motor.write(180); //Servo motor açı değeri olarak 180 dereceye döndürülür.
      delay(2000);//İki saniye beklenir.
      from_pi = 0;// "from_pi" değişkenine ilk değeri atanır.
  }

 }

}
