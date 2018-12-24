
#include <Wire.h>
#include <Adafruit_MotorShield.h>
#include <Servo.h>

// Create the motor shield object with the default I2C address
Adafruit_MotorShield AFMS = Adafruit_MotorShield();
// Or, create it with a different I2C address (say for stacking)
// Adafruit_MotorShield AFMS = Adafruit_MotorShield(0x61);

// Connect a stepper motor with 200 steps per revolution (1.8 degree)
// to motor port #2 (M3 and M4)
Adafruit_StepperMotor *myMotor = AFMS.getStepper(200, 1);

Servo tiltServo; // creates a servo object to control the tilting servo

int tiltServoPos = 0; // attaches the servo on pin 9 to the tiltServo object

int targetPosition = 0; //position of cup
int currentPosition = 0; //current position of motor
int difference = 0;  // difference between target position and current position
String sensorColorString = ""; // stores the string output by the Raspberry Pi



void setup() {
  tiltServo.attach(9);   // attaches the servo on pin 9 to the tiltServo object
  Serial.begin(9600);           // set up Serial library at 9600 bps
  Serial.println("Stepper test!");


  AFMS.begin();  // create with the default frequency 1.6KHz
  //AFMS.begin(1000);  // OR with a different frequency, say 1KHz

  myMotor->setSpeed(10);  // 10 rpm
}

void loop() {
   Serial.println("Single coil steps");
   myMotor->step(100, FORWARD, SINGLE);
   myMotor->step(100, BACKWARD, SINGLE);




//  if (Serial.available() > 0) {
//
//    sensorColorString = Serial.readString();
//    Serial.setTimeout(10);
//
//    Serial.print("I received: ");
//    Serial.println(sensorColorString);
//
//    targetPosition = sensorColorString.toInt();
//
//    tiltServo.write(90);
//    delay(4000);
//    tiltServo.write(50);
//     //Sets home position of the tiltServo to 95
//    colorToMotorSteps(); // moves stepper motor to correct position
//    delay(4000); //Waits 2 seconds
//    tiltServo.write(90); //Returns tilt servo to home position
//  }/

}

// Converts Raspberry Pi output to position of the servos
void colorToMotorSteps() {

  Serial.print(targetPosition);
  difference = targetPosition - currentPosition;
  if (difference > 0) {
    tiltServo.write(10);
    myMotor->step(difference,FORWARD,SINGLE);
  }
  if (difference < 0) {
    tiltServo.write(10);
    myMotor->step(difference,FORWARD,SINGLE);
  }

  currentPosition = targetPosition;


}
