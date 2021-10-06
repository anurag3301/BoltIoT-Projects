#include<Arduino.h>
void setup() {
  Serial.begin(9600);
  pinMode(11, INPUT);
}

void loop() {
  int s ;
  
  while(Serial.available()==0){
  }
  s = Serial.read();
  int x = digitalRead(11);
  Serial.flush();
  Serial.print(x);
  
}
