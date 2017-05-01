#include <Servo.h> 
#include <SPI.h>

#define led 13          //led is connected on pin 13
#define servopin 2      //servo is connected on pin 2

byte address = 0x00;    //address for digital pot over SPI bus
int CS= 10;             // configure pin 10 as SPI select line

Servo myservo;          

void setup() {
  
Serial.begin(9600);
pinMode(led,OUTPUT);
myservo.attach(servopin);
pinMode (CS, OUTPUT);
SPI.begin();

}

void loop() {
  
  if(Serial.available()>0){
    char c = Serial.read();
    if(c == 'A'){                 
      digitalWrite(led,1);
    }
    if(c == 'B'){
      digitalWrite(led,0);
    }
    
    if(c == 'C'){
     writeAngle(); 
    }
    if(c == 'D'){
     digitalPotWrite();
    }
  }

}

void writeAngle(){
  while(!Serial.available()>0);   //read angle value for servo 
  
  int c = Serial.read();
  myservo.write(c);
  Serial.print(c);
  Serial.println("Writing Servo");
}

int digitalPotWrite(){      
  while(!Serial.available()> 0);    //read resistance value for digital pot
  
  int value = Serial.read();
digitalWrite(CS, LOW);
SPI.transfer(address);
SPI.transfer(value);
digitalWrite(CS, HIGH);
}

