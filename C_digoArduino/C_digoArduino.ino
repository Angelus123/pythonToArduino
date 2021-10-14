#include <Servo.h>
const int led = 13;
const int led1 = 12;
char valor_dato = '1';
Servo servoThumb;



void setup()
{
  pinMode(led, OUTPUT);
  pinMode(led1, OUTPUT);
  digitalWrite (led, LOW);
  digitalWrite (led1, LOW);
  servoThumb.attach(7);
  Serial.begin(9600);
  Serial.println("Conexión Establecida");
}

void loop(){
  
  while(Serial.available())
  {
    valor_dato = Serial.read();
  }
  
  if (valor_dato == '0')
  {
   servoThumb.write(180); 
    digitalWrite (led, HIGH);
    digitalWrite (led1, LOW);
  }
  else if (valor_dato == '1')
  {
    servoThumb.write(0);
    digitalWrite (led, LOW);
    digitalWrite (led1, HIGH);
  }
}
