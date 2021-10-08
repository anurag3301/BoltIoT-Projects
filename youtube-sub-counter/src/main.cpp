#include<Arduino.h>

#include <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x3F, 16, 2);

void setup(){
    lcd.init();
    lcd.backlight();
    lcd.print("");
    Serial.begin(9600);
    Serial.setTimeout(50);
}

void loop(){
  String inString = "";
    String val[2] = {"", ""};
    if (Serial.available() > 0){
        lcd.clear();
        inString = Serial.readString();
        int index = 0;
        for (int i = 0; i < inString.length(); i++){
            if (inString[i] == '$'){
                index = 1;
                continue;
            }
            val[index] += inString[i];
        }
        lcd.setCursor(0, 0);
        lcd.print("Subs " + val[0]);
        lcd.setCursor(0, 1);
        lcd.print("Views " + val[1]);
    }
}

