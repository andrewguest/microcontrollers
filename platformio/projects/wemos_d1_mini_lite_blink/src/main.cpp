/*
VS Code PlatformIO keyboard shortcuts:

ctrl + alt + b -> build firmware
ctrl + alt + u -> upload firmware
ctrl + alt + s -> open serial monitor
*/

#include <Arduino.h>

#define LED 2  // define the pin that the LED is attached to (this is the onboard LED attached to pin #2)


void setup() {
  Serial.begin(115200);  // setup the serial communication
  pinMode(LED, OUTPUT);  // initialize the LED pin as an output
}

void loop() {
  digitalWrite(LED, LOW);  // turn the LED on
  Serial.println("LED on");
  delay(1000);  // wait for 1 second
  digitalWrite(LED, HIGH);  // turn the LED off
  Serial.println("LED off");
  delay(1000);  // wait for 1 second
}