const int led = 13;
const int led1 = 12;
int valor_dato = NULL;;

void setup()
{
  pinMode(led, OUTPUT);
  pinMode(led1, OUTPUT);
  digitalWrite (led, LOW);
  digitalWrite (led1, LOW);
  Serial.begin(9600);
//  Serial.println("Conexión Establecida");
}

void loop(){
  
  while(Serial.available())
  {
    valor_dato = Serial.read();
  }
  
  if (valor_dato)
  {
    digitalWrite (led, HIGH);
    digitalWrite (led1, HIGH);
  }
  else if (NULL)
  {
    digitalWrite (led, LOW);
    digitalWrite (led1, LOW);
  }
}

//int led =13;
//void setup() {
//  Serial.begin(9600);
//  pinMode(led, OUTPUT);
//}
//void loop(){
//  if(Serial.available()>0);
//  {
//    char option =Serial.read();
//    if (option == 's')
//      {
//      digitalWrite(led,HIGH);
//      
//      }
//      else 
//      {
//        digitalWrite(led, LOW);
//      }
//    }
//}
