#include "SleepyPi2.h"
#include <LowPower.h>
 
void setup() {
 
   // Configure "Standard" LED pin
   pinMode(17, OUTPUT); 
   digitalWrite(LED_PIN,LOW); // Switch off LED
}
 
void loop() {
 
    // Enter idle state for 8 s with the rest of peripherals turned off
    SleepyPi.idle(SLEEP_8S, ADC_OFF)
 
   // Do something here
   // Example: Read sensor, data logging, data transmission.
   Serial.println("I've Just woken up");
   digitalWrite(17,HIGH); // Switch on LED
   delay(350); 
   digitalWrite(17,LOW); // Switch off LED
 
}