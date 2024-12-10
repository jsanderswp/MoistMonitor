// C++ code
//

#include "Adafruit_seesaw.h"

Adafruit_seesaw ss;

void setup() {
  Serial.begin(115200);

  if (!ss.begin(0x36)) {
    while(1) delay(1); // Halt execution if the sensor isn't found
  }
}

void loop() {
  uint16_t capread = ss.touchRead(0);

  Serial.println(capread); // Send only the raw capread value
  delay(100); // Optional: Control data output frequency
}
