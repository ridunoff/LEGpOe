#include <Servo.h>

Servo tiltServo;    // creates a servo object to control the tilting servo
Servo spinServo;    // creates a servo object to control the cup spinning servo

int tiltServoPos = 0;    // stores the tiltServo position
int spinServoPos = 0;    // stores the spinServo position

int sensorValue = 0;           // stores the value output by the Raspberry Pi
String sensorColorString = ""; // stores the string output by the Raspberry Pi

void setup() {
  tiltServo.attach(9);  // attaches the servo on pin 9 to the tiltServo object
  spinServo.attach(8);  // attaches the servo on pin 8 to the spinServo object
  Serial.begin(9600); //Initialize the serial monitor
}

void loop() {
  //Reads the serial monitor input only when data is sent
  if (Serial.available() > 0) {
    // read the incoming byte:
    sensorColorString = Serial.readString();
    Serial.setTimeout(10);

    Serial.print("I received: ");
    Serial.println(sensorColorString);

    sensorValue = sensorColorString.toInt(); //Converts the recieved string to an int

    tiltServo.write(95); //Sets home position of the tiltServo to 95
    colorToServoValue(); //Moves both servos dependant on the int entered
    delay(2000); //Waits 2 seconds
    tiltServo.write(95); //Returns tilt servo to home position
  }
}

//Calibration for the base servo
void testServo1(){
    Serial.print(sensorValue);
    spinServoPos = sensorValue;
    spinServo.write(spinServoPos);
}

//Calibration for the tilt servo
void testServo2(){
    Serial.print(sensorValue);
    tiltServoPos = sensorValue;
    tiltServo.write(tiltServoPos);
}

void colorToServoValue(){   //Converts the Raspberry Pi output to positions of the servos
   Serial.print(sensorValue);
   if(sensorValue == 1){
      tiltServoPos = 120;
      spinServoPos = 5;
      spinServo.write(spinServoPos);
      delay(2000);
      tiltServo.write(tiltServoPos);
   }
   if(sensorValue == 2){
      tiltServoPos = 120;
      spinServoPos = 90;
      spinServo.write(spinServoPos);
      delay(2000);
      tiltServo.write(tiltServoPos);
   }
   if(sensorValue == 3){
      tiltServoPos = 70;
      spinServoPos = 5;
      spinServo.write(spinServoPos);
      delay(2000);
      tiltServo.write(tiltServoPos);
   }
   if(sensorValue == 4){
      tiltServoPos = 70;
      spinServoPos = 90;
      spinServo.write(spinServoPos);
      delay(2000);
      tiltServo.write(tiltServoPos);
   }
}
