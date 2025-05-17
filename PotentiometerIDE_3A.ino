const int potPin = A0;  // Define the pin connected to the potentiometer
       // Variable to store the potentiometer value
const int ledPin = 9;
void setup() {
    Serial.begin(9600);  // Initialize serial communication
    pinMode(9, OUTPUT);
}

void loop() {
    int potValue = analogRead(potPin);  // Read the potentiometer value
    Serial.println(potValue);     // Print the value to the Serial Monitor
    int ledbrightness = map(potValue,0, 1023, 255, 0);
    analogWrite(ledPin, ledbrightness);
    delay(500);                      // Small delay for readability
}