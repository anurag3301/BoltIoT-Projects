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
      lcd.setCursor(0, 0);
      lcd.print("Subs: ");
      lcd.setCursor(0, 1);
      lcd.print("Viewes: ");
}

