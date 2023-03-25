void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
  pinMode(A0, OUTPUT);
}

void loop()
{
  
  int sv = analogRead(A0);
  Serial.println(sv);
  if (sv>=0)
  {
    digitalWrite(sv,HIGH);}
  Serial.println(sv);
  delay(1);  }

