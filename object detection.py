#include<LiquidCrystal.h>
LiquidCrystal lcd(0,1,2,3,4,5);
void setup()
{
  lcd.begin(16,2);
  pinMode(12,INPUT);
  pinMode(13,OUTPUT);
  pinMode(10,OUTPUT);
  lcd.print("OBJECT DETECTED ");
}
void loop()
{
  long t;
  int d;
  digitalWrite(13,HIGH);
  delayMicroseconds(10);
  digitalWrite(13,LOW);
  t=pulseIn(12,HIGH);
  d=(t/2)*0.0341;
  lcd.setCursor(1,1);
  lcd.print(d);
  lcd.print("cm");
  lcd.print("   ");
  if (d < 300)
   {
     tone(10,400,200);
   }
               
    delay(200);
}

  
