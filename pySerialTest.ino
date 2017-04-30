#include <Servo.h> 
#include <SPI.h>

#define led 13
#define servopin 2
byte address = 0x00;
int CS= 10;

Servo myservo;

void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
pinMode(led,OUTPUT);
myservo.attach(servopin);
pinMode (CS, OUTPUT);
SPI.begin();

}

void loop() {
  
  if(Serial.available()>0)
  {
    char c = Serial.read();
    if(c == 'A')
    {
      digitalWrite(led,1);
    }
    if(c == 'B')
    {
      digitalWrite(led,0);
    }
    
    if(c == 'C')
    {
     writeAngle(); 
    }
    if(c == 'D')
    {
     digitalPotWrite();
    }
  }

}

void writeAngle()
{
  while(!Serial.available()>0);
  
  int c = Serial.read();
  myservo.write(c);
  Serial.print(c);
  Serial.println("Writing Servo");
}

int digitalPotWrite()
{
  while(!Serial.available()>0);
  
  int value = Serial.read();
digitalWrite(CS, LOW);
SPI.transfer(address);
SPI.transfer(value);
digitalWrite(CS, HIGH);
}

