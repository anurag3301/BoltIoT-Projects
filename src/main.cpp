#include<Arduino.h>
void setup() {
  Serial.begin(9600);
  pinMode(11, INPUT);
}

void loop() {
  int s ;
  
  while(Serial.available()==0){            //wait for input in serial monitor
  }
  s = Serial.read();
  int x = digitalRead(11);
  Serial.print(x);
  
}
