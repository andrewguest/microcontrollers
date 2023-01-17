#include <Wire.h>
#include <Adafruit_ILI9341.h>

#define TFT_DC 15
#define TFT_CS 33
#define TFT_MOSI 23
#define TFT_CLK 18
#define TFT_RST 5
#define TFT_MISO 19

Adafruit_ILI9341 tft = Adafruit_ILI9341(TFT_CS, TFT_DC, TFT_MOSI, TFT_CLK, TFT_RST, TFT_MISO);

void setup() {
  tft.begin();
  tft.setRotation(3);
  tft.fillScreen(ILI9341_BLACK);
  tft.setTextSize(2);
  tft.setCursor(10, 10);
  tft.setTextColor(ILI9341_WHITE);
  tft.print("Hello, World!");
}

void loop() {
}
