#include<Arduino.h>
void setup() {
  Serial.begin(9600);
  pinMode(11, INPUT);
  pinMode(12, OUTPUT);
  

}

void loop() {

  digitalWrite(12, HIGH);
  delay(500);
  digitalWrite(12, LOW);
  delay(500);
  digitalWrite(12, HIGH);
  delay(5000);
  
  
  // while(Serial.available()==0){
  // }
  // s = Serial.read();
  // int x = digitalRead(11);
  // Serial.flush();
  // Serial.print(x);
  
}
